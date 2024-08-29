"""
Insta485 user view.

URLs include:
/comments/
"""

import flask
from flask import request
import insta485
from insta485.views.account import redirect_to_target, check_login


@insta485.app.route('/comments/', methods=['POST'])
@check_login
def edit_comments():
    """Create or delete comments."""
    operation = request.form['operation']

    if operation == 'create':
        create_comment()
    if operation == 'delete':
        delete_comment()
    return redirect_to_target()


def create_comment():
    """Create a comment for postid."""
    postid = request.form['postid']
    text = request.form['text']
    if text is None:
        flask.abort(400)
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    connection.execute(
        'INSERT INTO comments(owner, postid, text) '
        "VALUES (?, ?, ?)",
        (logname, postid, text)
    )


def delete_comment():
    """Delete a comment for commentid."""
    commentid = request.form['commentid']
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    comment = get_comment_by_id(commentid)

    if comment is None:
        flask.abort(400)

    print(comment['owner'])
    print(logname)
    if comment['owner'] != logname:
        flask.abort(403)

    connection.execute(
        'DELETE FROM comments '
        "WHERE commentid = ?",
        commentid
    )


def get_comment_by_id(commentid):
    """Return if a comment is exit and owned by logged in user."""
    connection = insta485.model.get_db()
    comment = connection.execute(
        'SELECT * FROM comments '
        "WHERE commentid = ? ",
        (commentid,)
    ).fetchone()
    return comment
