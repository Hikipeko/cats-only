"""
Insta485 user view.

URLs include:
/account/
"""

import hashlib
import os
import pathlib
import uuid
from functools import wraps
import flask
from flask import session, redirect, url_for, request, render_template
import insta485


def valid_user(username, connection):
    """Whether the user is in the database."""
    is_valid = connection.execute(
        'SELECT COUNT(*) AS cnt FROM users WHERE users.username= ?',
        (username, )
    ).fetchone()['cnt']
    return is_valid == 1


def check_login(func):
    """Redirect to login page if not login."""
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'logname' not in session:
            return redirect(url_for('show_login'))
        return func(*args, **kwargs)
    return decorated


def must_login(func):
    """Check user must be logged in, otherwise abort 403."""
    @wraps(func)
    def decorated(*args, **kwargs):
        if 'logname' not in session:
            flask.abort(403)
        return func(*args, **kwargs)
    return decorated


@insta485.app.route('/accounts/login/', methods=['GET'])
def show_login():
    """Show the login form."""
    if 'logname' in session:
        # redirect to / page
        return redirect(url_for('show_index'))
    return render_template("login.html")


@insta485.app.route('/accounts/logout/', methods=['POST'])
def show_logout():
    """Log out the user."""
    session.clear()
    return redirect(url_for('show_login'))


@insta485.app.route('/accounts/create/', methods=['GET'])
def show_create():
    """Show the create account form."""
    if 'logname' in session:
        redirect(url_for('show_edit'))
    return render_template('create.html')


@insta485.app.route('/accounts/delete/', methods=['GET'])
@must_login
def show_delete():
    """Show the delete account form."""
    logname = session.get('logname')
    context = {'logname': logname}
    return render_template('delete.html', **context)


@insta485.app.route('/accounts/edit/', methods=['GET'])
@must_login
def show_edit():
    """Show the edit account form."""
    logname = session.get('logname')
    connection = insta485.model.get_db()
    email = connection.execute(
        'SELECT email FROM users WHERE username = ?', (logname,)
    ).fetchone()['email']
    context = {'logname': logname, 'email': email}
    return render_template('edit.html', **context)


@insta485.app.route('/accounts/password/', methods=['GET'])
@must_login
def show_password():
    """Show the edit password form."""
    logname = session.get('logname')
    context = {'logname': logname}
    return render_template('password.html', **context)


def verify_password(password, password_encrypted):
    """Password verification."""
    salt = password_encrypted.split('$')[1]
    return encrypt_password(password, salt) == password_encrypted


def redirect_to_target():
    """Redirect page to url."""
    target = request.args.get('target')
    if target is None:
        return flask.redirect(url_for('show_index'))
    return flask.redirect(target)


def login():
    """Login the user."""
    username = request.form.get('username')
    password_input = request.form.get('password')
    # check not empty
    if not (username and password_input):
        flask.abort(400)
    connection = insta485.model.get_db()
    password = connection.execute(
        'SELECT password FROM users WHERE username = ?', (username,)
    ).fetchone()
    if not password:
        flask.abort(403)  # user not found
    password_db = password['password']
    if verify_password(password_input, password_db):
        # set a session cookie
        session['logname'] = username
    else:
        flask.abort(403)  # incorrect password
    return redirect_to_target()


def save_file(fileobj):
    """Save the fileobj to the users upload directory."""
    filename = fileobj.filename
    stem = uuid.uuid4().hex
    suffix = pathlib.Path(filename).suffix
    uuid_basename = f"{stem}{suffix}"
    # Save to disk
    path = insta485.app.config["UPLOAD_FOLDER"] / uuid_basename
    fileobj.save(path)
    return uuid_basename


def encrypt_password(password, salt=None):
    """Encrypt the password."""
    algorithm = 'sha512'
    if not salt:
        salt = uuid.uuid4().hex
    hash_obj = hashlib.new(algorithm)
    password_salted = salt + password
    hash_obj.update(password_salted.encode('utf-8'))
    password_hash = hash_obj.hexdigest()
    password_db_string = "$".join([algorithm, salt, password_hash])
    return password_db_string


def create_account():
    """Create a new account."""
    username = request.form.get('username')
    password = request.form.get('password')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    fileobj = request.files['file']
    uuid_basename = save_file(fileobj)
    if not (username and password and fullname and email):
        flask.abort(400)
    connection = insta485.model.get_db()
    if connection.execute(
        'SELECT COUNT(*) AS cnt FROM users '
        'WHERE username = ? ', (username,)
    ).fetchone()['cnt'] != 0:
        flask.abort(409)  # username exists
    # encrypt password
    password_encrypted = encrypt_password(password)
    connection = insta485.model.get_db()
    connection.execute(
        'INSERT INTO users(username, fullname, email, filename, password) '
        'VALUES (?, ?, ?, ?, ?) ',
        (username, fullname, email, uuid_basename, password_encrypted))
    session['logname'] = username
    return redirect_to_target()


@must_login
def delete_account():
    """Delete login account."""
    logname = session.get('logname')
    connection = insta485.model.get_db()
    user_img_url = connection.execute(
        "SELECT users.filename FROM users WHERE username = ? ", (logname,)
    ).fetchone()["filename"]
    os.remove(os.path.join(insta485.app.config["UPLOAD_FOLDER"], user_img_url))
    post_picture = connection.execute(
        "SELECT filename FROM posts WHERE owner = ? ", (logname,)
    ).fetchall()
    for picture in post_picture:
        picture = picture['filename']
        os.remove(os.path.join(insta485.app.config["UPLOAD_FOLDER"],
                               picture))
    connection.execute("DELETE FROM users WHERE username = ?", (logname,))
    session.clear()
    return redirect_to_target()


@must_login
def edit_account():
    """Edit account information."""
    logname = session.get('logname')
    fullname = request.form.get('fullname')
    email = request.form.get('email')
    connection = insta485.model.get_db()
    if not (email and fullname and logname):
        flask.abort(400)
    # edit user_img if it exists
    fileobj = request.files['file']
    if fileobj:
        # save new avatar
        uuid_basename = save_file(fileobj)
        # delete old avatar
        old_file = connection.execute(
            'SELECT filename FROM users WHERE username = ? ',
            (logname,)
        ).fetchone()['filename']
        # update db user avatar filename
        (insta485.app.config["UPLOAD_FOLDER"] / old_file).unlink()
        connection.execute(
            'UPDATE users SET filename = ? '
            'WHERE username = ? ', (uuid_basename, logname)
        )
    connection.execute(
        'UPDATE users SET email= ?, fullname= ? '
        'WHERE username = ? ', (email, fullname, logname))
    return redirect_to_target()


@must_login
def update_password():
    """Update password."""
    logname = session['logname']
    new_password1 = request.form.get('new_password1')
    new_password2 = request.form.get('new_password2')
    password = request.form.get('password')
    if not (new_password1 and new_password2 and password):
        flask.abort(400)
    # password doesnt match
    if new_password1 != new_password2:
        flask.abort(401)
    # check old password
    connection = insta485.model.get_db()
    old_password_hash = connection.execute(
        'SELECT password FROM users WHERE username = ? ', (logname,)
    ).fetchone()['password']
    if not verify_password(password, old_password_hash):
        flask.abort(403)
    # update new password in database
    new_password_hash = encrypt_password(new_password1)
    connection.execute(
        'UPDATE users SET password = ? WHERE username = ? ',
        (new_password_hash, logname)
    )
    return redirect_to_target()


@insta485.app.route('/accounts/', methods=['POST'])
def account_post():
    """Handle post edition."""
    operation = request.form.get('operation')
    if operation == 'login':
        return login()
    if operation == 'create':
        return create_account()
    if operation == 'delete':
        return delete_account()
    if operation == 'edit_account':
        return edit_account()
    if operation == 'update_password':
        return update_password()
    return flask.abort(400)
