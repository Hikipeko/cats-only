"""
Insta485 index (main) view.

URLs include:
/
"""

from datetime import datetime
import flask
import arrow
import insta485
from insta485.views.account import check_login


@insta485.app.route('/', methods=['GET'])
@check_login
def show_index():
    """Display / route."""
    # Connect to database
    connection = insta485.model.get_db()
    # Check out config.json to see what data should be passed to the template
    logname = flask.session['logname']
    # add posts
    posts = connection.execute(
        'SELECT postid, owner, users.filename AS owner_img_url, '
        'posts.filename AS img_url, posts.created FROM posts '
        'JOIN users ON users.username=posts.owner '
        'WHERE users.username = ? OR users.username IN '
        '(SELECT username2 FROM following WHERE username1 = ?) '
        'ORDER by postid DESC',
        (logname, logname)
    ).fetchall()
    # create a dictionary to trace likes of post by postid
    likes_count_list = connection.execute(
        'SELECT postid, COUNT(*) AS cnt FROM likes GROUP BY postid'
    ).fetchall()
    likes_count = {}
    for item in likes_count_list:
        likes_count[item['postid']] = item['cnt']
    past = arrow.utcnow()  # .shift(hours=-4)
    for post in posts:
        # add timestamp as key
        post['timestamp'] = past.humanize(
            datetime.strptime(post["created"], '%Y-%m-%d %H:%M:%S'))
        del post['created']
        # add likes as key
        like_cnt = likes_count.get(post["postid"])
        post['likes'] = 0 if like_cnt is None else like_cnt
        post['like_or_not'] = connection.execute(
            'SELECT COUNT(*) AS cnt FROM likes WHERE postid = ? '
            'AND owner = ? ', (post["postid"], logname)
        ).fetchone()['cnt'] == 1
        # add comments as key
        post["comments"] = connection.execute(
            'SELECT owner, text FROM comments WHERE postid = ? '
            'ORDER BY commentid', (post["postid"],)
        ).fetchall()
    # Add database info to context
    context = {"logname": logname, "posts": posts}
    return flask.render_template("index.html", **context)
