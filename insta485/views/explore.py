"""
Insta485 user view.

URLs include:
/explore/
"""

import flask
import insta485
from insta485.views.account import check_login


@insta485.app.route('/explore/', methods=['GET'])
@check_login
def show_explore():
    """Display explore route."""
    # Connect to database
    connection = insta485.model.get_db()
    logname = flask.session.get('logname')
    # Query database: not_following.username, not_following.user_img_url
    # username1 follows username2
    # select username
    # s.t. username != logname && username !in {u2: logname follows u2}
    not_followings = connection.execute(
        'SELECT username, filename AS user_img_url '
        'FROM users '
        'WHERE NOT users.username = ? AND NOT users.username IN '
        '(SELECT following.username2 FROM following '
        'WHERE following.username1 = ?)',
        (logname, logname)
    ).fetchall()
    context = {"logname": logname,
               "not_following": not_followings,
               }
    return flask.render_template("explore.html", **context)
