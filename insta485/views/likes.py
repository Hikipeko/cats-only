"""
Insta485 user view.

URLs include:
/likes/?target=URL
"""

import flask
from flask import request
import insta485
from insta485.views.account import redirect_to_target, check_login


@insta485.app.route('/likes/', methods=['POST'])
@check_login
def edit_likes():
    """Create or delete likes."""
    operation = request.form['operation']
    postid = request.form['postid']
    if operation == 'like':
        create_like(postid)
    if operation == 'unlike':
        delete_like(postid)
    return redirect_to_target()


def create_like(postid):
    """Create a like for postid."""
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    if is_post_exist(postid):
        flask.abort(409)
    connection.execute(
        'INSERT INTO likes(owner, postid) '
        "VALUES (?, ?)",
        (logname, postid)
    )


def delete_like(postid):
    """Delete a like for postid."""
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')

    if not is_post_exist(postid):
        flask.abort(409)
    connection.execute(
        'DELETE FROM likes '
        "WHERE owner = ? AND postid = ?",
        (logname, postid)
    )


def is_post_exist(postid):
    """Return if a post is already liked."""
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    like = connection.execute(
        'SELECT * FROM likes '
        "WHERE owner = ? AND postid = ?",
        (logname, postid)
    ).fetchone()
    return like is not None
