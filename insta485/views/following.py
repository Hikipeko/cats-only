"""
Insta485 user view.

URLs include:
/users/<username>/following/
/following/
"""

import flask
from flask import request
import insta485
from insta485.views.account import check_login, redirect_to_target, valid_user


@insta485.app.route('/users/<username>/following/', methods=['GET'])
@check_login
def show_following(username):
    """Display following route."""
    # Connect to database
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    # Check if username exists in database
    if valid_user(username, connection) == 0:
        flask.abort(404)
    # Query database: following.username, following.user_img_url
    # username1 follows username2
    followings = connection.execute(
        'SELECT username2 AS username, users.filename AS user_img_url '
        'FROM following '
        'JOIN users ON users.username = following.username2 '
        'WHERE following.username1 = ?',
        (username, )
    ).fetchall()
    # Set logname_follows_username bool
    for following in followings:
        is_following = connection.execute(
            'SELECT COUNT(username1) AS cnt FROM following '
            'WHERE following.username1 = ? AND following.username2 = ?',
            (logname, following["username"])
        ).fetchone()['cnt']
        following["logname_follows_username"] = (is_following == 1)
    context = {"logname": logname,
               "username": username,
               "following": followings,
               }
    return flask.render_template("following.html", **context)


@insta485.app.route('/following/', methods=['POST'])
@check_login
def edit_following():
    """Follow or unfollow a user."""
    operation = request.form['operation']
    username = request.form['username']
    if operation == 'follow':
        create_follow(username)
    if operation == 'unfollow':
        delete_follow(username)
    return redirect_to_target()


def create_follow(username):
    """Follow the user with username."""
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    if is_follow(username):
        flask.abort(409)
    connection.execute(
        'INSERT INTO following(username1, username2) '
        "VALUES (?, ?)",
        (logname, username)
    )


def delete_follow(username):
    """Unfollow the user with username."""
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')

    if not is_follow(username):
        flask.abort(409)
    connection.execute(
        'DELETE FROM following '
        "WHERE username1 = ? AND username2 = ?",
        (logname, username)
    )


def is_follow(username):
    """Return if the user is already followed."""
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    follow = connection.execute(
        'SELECT * FROM following '
        "WHERE username1 = ? AND username2 = ?",
        (logname, username)
    ).fetchone()
    return follow is not None
