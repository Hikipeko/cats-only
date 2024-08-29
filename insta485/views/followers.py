"""
Insta485 followers view.

URLs include:
/users/<username>/followers/
"""

import flask
import insta485
from insta485.views.account import check_login, valid_user


@insta485.app.route('/users/<username>/followers/', methods=['GET'])
@check_login
def show_followers(username):
    """Display followers route."""
    # Connect to database
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    # Check if username exists in database
    if valid_user(username, connection) == 0:
        flask.abort(404)
    # Query database: follower.username, follower.user_img_url
    # username1 follows username2
    followers = connection.execute(
        'SELECT username1 AS username, users.filename AS user_img_url '
        'FROM following '
        'JOIN users ON users.username = following.username1 '
        'WHERE following.username2 = ?',
        (username, )
    ).fetchall()
    # Set logname_follows_username bool
    for follower in followers:
        is_following = connection.execute(
            'SELECT COUNT(username1) AS cnt FROM following '
            'WHERE following.username1 = ? AND following.username2 = ?',
            (logname, follower["username"])
        ).fetchone()['cnt']
        follower["logname_follows_username"] = (is_following == 1)
    context = {"logname": logname,
               "username": username,
               "followers": followers,
               }
    return flask.render_template("followers.html", **context)
