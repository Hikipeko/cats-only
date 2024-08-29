"""REST API for likes."""
import flask
from flask import request, session
import insta485
from insta485.api.auth import check_auth, InvalidUsage


@insta485.app.route('/api/v1/likes/', methods=['POST'])
@check_auth
def create_like():
    """Return like on postid & auth.

    If does not exist, create and return it with 201 response;
    otherwise, return it with 200 response.
    Example:
    {
        "likeid": 6,
        "url": "/api/v1/likes/6/"
    }
    """
    postid = request.args.get('postid', type=int)
    connection = insta485.model.get_db()
    post_exists(postid, connection)
    logname = session['logname']
    like_obj = connection.execute(
        'SELECT likeid '
        'FROM likes '
        'WHERE owner = ? AND postid = ?',
        (logname, postid)
    ).fetchone()
    if like_obj is None:
        # create when not exists
        connection.execute(
            'INSERT INTO likes(owner, postid) '
            'VALUES (?, ?)',
            (logname, postid)
        )
        likeid = connection.execute(
            'SELECT last_insert_rowid() AS id '
            'FROM likes'
        ).fetchone()['id']
        context = {
            "likeid": likeid,
            "url": flask.request.path + str(likeid) + '/'
        }
        # set 201 response
        return flask.jsonify(**context), 201
    likeid = like_obj['likeid']
    context = {
        "likeid": likeid,
        "url": flask.request.path + str(likeid) + '/'
    }
    # set 200 response
    return flask.jsonify(**context), 200


@insta485.app.route('/api/v1/likes/<int:likeid>/', methods=['DELETE'])
@check_auth
def delete_like(likeid):
    """Delete like specified by likeid.

    Return 204 on success;
    return 404 if likeid does not exist;
    return 403 if user does not own like.
    """
    connection = insta485.model.get_db()
    logname = session['logname']
    like_obj = connection.execute(
        'SELECT * '
        'FROM likes '
        'WHERE likeid = ?',
        (likeid, )
    ).fetchone()
    if like_obj is None:
        raise InvalidUsage('Not Found', 404)
    if like_obj['owner'] != logname:
        raise InvalidUsage('Forbidden', 403)
    connection.execute(
        'DELETE FROM likes '
        'WHERE owner = ? AND likeid = ?',
        (logname, likeid)
    )
    return '', 204


def post_exists(postid, connection):
    """Ensure postid exists in db."""
    # not required in spec?
    exists = connection.execute(
        'SELECT COUNT(*) AS cnt '
        'FROM posts '
        'WHERE postid = ?',
        (postid, )
    ).fetchone()['cnt']
    if exists == 0:
        raise InvalidUsage('Post does not exist', 404)
