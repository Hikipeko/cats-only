"""REST API for comments."""
import flask
from flask import request, session
import insta485
from insta485.api.auth import check_auth, InvalidUsage


@insta485.app.route('/api/v1/comments/', methods=['POST'])
@check_auth
def create_comment():
    """Return comment on postid & auth.

     Return 201 on success.
    Example:
    {
       "commentid": 8,
        "lognameOwnsThis": true,
        "owner": "awdeorio",
        "ownerShowUrl": "/users/awdeorio/",
        "text": "Comment sent from httpie",
        "url": "/api/v1/comments/8/"
    }
    """
    postid = request.args.get('postid', type=int)
    connection = insta485.model.get_db()
    logname = session['logname']
    text = request.json.get("text")
    print(f"INSERT INTO comments({logname}, {postid}, {text})")
    connection.execute(
        'INSERT INTO comments (owner, postid, text) '
        'VALUES (?, ?, ?)',
        (logname, postid, text)
    )
    commentid = connection.execute(
        'SELECT last_insert_rowid() AS id '
        'FROM comments'
    ).fetchone()['id']

    context = {
        "commentid": commentid,
        "lognameOwnsThis": True,
        "owner": logname,
        "ownerShowUrl": f"/users/{logname}/",
        "text": text,
        "url": f"/api/v1/comments/{commentid}/"
    }
    return flask.jsonify(**context), 201


@insta485.app.route('/api/v1/comments/<int:commentid>/', methods=['DELETE'])
@check_auth
def delete_comment(commentid):
    """Delete comment by comment id.

    Return 204 on success.
    If the commentid does not exist, return 404.
    If the user doesn't own the comment, return 403.
    """
    connection = insta485.model.get_db()
    logname = session['logname']
    comment_obj = connection.execute(
        'SELECT * '
        'FROM comments '
        'WHERE commentid = ?',
        (commentid, )
    ).fetchone()
    if comment_obj is None:
        raise InvalidUsage('Not Found', 404)
    if comment_obj['owner'] != logname:
        raise InvalidUsage('Forbidden', 403)
    connection.execute(
        'DELETE FROM comments '
        'WHERE owner = ? AND commentid = ?',
        (logname, commentid)
    )
    return "", 204
