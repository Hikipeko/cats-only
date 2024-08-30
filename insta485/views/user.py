"""
Insta485 user view.

URLs include:
/users/<username>/
"""

import flask
import insta485
from insta485.views.account import check_login, valid_user


@insta485.app.route('/users/<username>/', methods=['GET'])
@check_login
def show_user(username):
    """Display users route."""
    # Connect to database
    logname = flask.session.get('logname')
    connection = insta485.model.get_db()
    if valid_user(username, connection) == 0:
        flask.abort(404)
    # Query database: fullname, post.postid, post.img_url;
    # should belong to username
    fullname = connection.execute(
        'SELECT fullname FROM users '
        'WHERE users.username = ?',
        (username, )
    ).fetchone()['fullname']
    user_img_url = connection.execute(
        'SELECT filename AS user_img_url '
        'FROM users '
        'WHERE users.username = ?',
        (username, )
    ).fetchone()['user_img_url']
    partial_posts = connection.execute(
        'SELECT postid, posts.filename AS img_url FROM posts '
        'WHERE posts.owner = ?'
        'ORDER by postid DESC',
        (username, )
    ).fetchall()
    # count #posts, #followers, #following
    total_posts = len(partial_posts)
    # username1 follows username2
    followers = connection.execute(
        'SELECT COUNT(following.username1) AS cnt FROM following '
        'WHERE following.username2 = ?',
        (username, )
    ).fetchone()["cnt"]
    following = connection.execute(
        'SELECT COUNT(following.username2) AS cnt FROM following '
        'WHERE following.username1 = ?',
        (username, )
    ).fetchone()["cnt"]
    is_following = connection.execute(
        'SELECT COUNT(username1) AS cnt FROM following '
        'WHERE following.username1 = ? AND following.username2 = ?',
        (logname, username)
    ).fetchone()['cnt']
    logname_follows_username = (is_following == 1)
    context = {"logname": logname,
               "username": username,
               "logname_follows_username": logname_follows_username,
               "fullname": fullname,
               "total_posts": total_posts,
               "followers": followers,
               "following": following,
               "posts": partial_posts,
               "user_img_url": user_img_url
               }
    return flask.render_template("user.html", **context)
