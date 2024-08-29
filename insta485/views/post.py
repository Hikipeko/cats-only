"""
Insta485 user view.

URLs include:
/posts/<postid>/
/posts/
"""

import os
import pathlib
import uuid
from datetime import datetime
import flask
from flask import request
import arrow
import insta485
from insta485.views.account import check_login


@insta485.app.route('/posts/<postid>/', methods=['GET'])
@check_login
def show_post(postid):
    """Display post route."""
    # Connect to database
    connection = insta485.model.get_db()
    # Check out config.json to see what data should be passed to the template
    logname = flask.session.get('logname')
    # add post
    post = connection.execute(
        'SELECT postid, owner, users.filename AS owner_img_url, '
        'posts.filename AS img_url, posts.created FROM posts '
        'JOIN users ON users.username=posts.owner '
        'WHERE postid = ?',
        (postid, )
    ).fetchone()
    if post is None:
        flask.abort(404)  # not required in spec?
    # count single post num of like
    like_cnt = connection.execute(
        'SELECT COUNT(*) AS cnt FROM likes '
        'WHERE likes.postid = ?',
        (postid, )
    ).fetchone()['cnt']
    past = arrow.utcnow()
    # add timestamp as key
    post['timestamp'] = past.humanize(
        datetime.strptime(post["created"], '%Y-%m-%d %H:%M:%S'))
    del post['created']
    # add likes as key
    post['likes'] = 0 if like_cnt is None else like_cnt
    post['like_or_not'] = connection.execute(
        'SELECT COUNT(*) AS cnt FROM likes '
        'WHERE postid = ? AND owner = ? ', (post["postid"], logname)
    ).fetchone()['cnt'] == 1
    # add comments as key
    post["comments"] = connection.execute(
        'SELECT owner, text, commentid FROM comments WHERE postid = ? '
        'ORDER BY commentid', (post["postid"],)
    ).fetchall()
    url = '/posts/'+postid+'/'
    # Add database info to context
    context = {"logname": logname,
               "post": post,
               "url": url,
               #    "postid": postid,
               #    "img_url" : post["img_url"],
               #    "owner": post["owner"],
               #    "owner_img_url": post["owner_img_url"],
               #    "timestamp": post["timestamp"],
               #    "likes": post["likes"],
               #    "comments": post["comments"],
               #    "like_or_not": post["like_or_not"]
               }
    return flask.render_template("post.html", **context)


@insta485.app.route('/posts/', methods=['POST'])
@check_login
def edit_posts():
    """Create or delete posts."""
    operation = request.form['operation']
    logname = flask.session.get('logname')

    if operation == 'create':
        create_post()
    if operation == 'delete':
        delete_post()

    target = request.args.get('target')
    if target is None:
        return flask.redirect('/users/' + logname + '/')
    return flask.redirect(target)


def create_post():
    """Create a post for postid."""
    # Unpack flask object
    fileobj = request.files['file']
    filename = fileobj.filename

    # Compute base name (filename without directory).  We use a UUID to avoid
    # clashes with existing files,
    # and ensure that the name is compatible with the filesystem.
    stem = uuid.uuid4().hex
    suffix = pathlib.Path(filename).suffix
    uuid_basename = f"{stem}{suffix}"
    if fileobj is None:
        flask.abort(400)

    # Save the image to disk
    path = insta485.app.config["UPLOAD_FOLDER"]/uuid_basename
    fileobj.save(path)

    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    connection.execute(
        'INSERT INTO posts(owner, filename) '
        "VALUES (?, ?)",
        (logname, uuid_basename)
    )


def delete_post():
    """Delete a post for postid."""
    postid = request.form['postid']
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')

    post = get_post_by_id(postid)

    if post is None:
        flask.abort(400)
    if post['owner'] != logname:
        flask.abort(403)

    path = insta485.app.config["UPLOAD_FOLDER"]/post['filename']
    os.remove(path)

    connection.execute(
        'DELETE FROM posts '
        "WHERE postid = ?",
        postid
    )


def get_post_by_id(postid):
    """Return if a post is exit and owned by logged in user."""
    connection = insta485.model.get_db()
    post = connection.execute(
        'SELECT * FROM posts '
        "WHERE postid = ?",
        postid
    ).fetchone()
    return post
