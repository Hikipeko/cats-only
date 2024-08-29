"""REST API for posts."""
import flask
from flask import jsonify, request, session
import insta485
from insta485.api.auth import check_auth, InvalidUsage


@insta485.app.route('/api/v1/', methods=['GET'])
def get_main():
    """Return a list of services available."""
    context = {
        "comments": "/api/v1/comments/",
        "likes": "/api/v1/likes/",
        "posts": "/api/v1/posts/",
        "url": "/api/v1/"
    }
    return jsonify(**context)


@insta485.app.route('/api/v1/posts/', methods=['GET'])
@check_auth
def get_posts():
    """Return the 10 newest posts."""
    size = request.args.get('size', default=10, type=int)
    page = request.args.get('page', default=0, type=int)
    if size < 0 or page < 0:
        raise InvalidUsage('Bad Request', status_code=400)
    # Get postid_lte
    connection = insta485.model.get_db()
    postid_max = connection.execute(
        'SELECT MAX(postid) AS postid_max FROM posts'
    ).fetchone()['postid_max']
    postid_lte = request.args.get("postid_lte", default=postid_max, type=int)
    # Get posts from the database
    logname = session['logname']
    posts = connection.execute(
        'SELECT postid FROM posts '
        'WHERE (owner = ? '
        'OR owner IN (SELECT username2 FROM following WHERE username1 = ?)) '
        'AND postid <= ? '
        'ORDER BY postid DESC '
        'LIMIT ? OFFSET ?',
        (logname, logname, postid_lte, size, page * size)
    ).fetchall()
    for post in posts:
        post['url'] = f"/api/v1/posts/{post['postid']}/"
    if len(posts) == size:
        # have a next page to show
        next_u = f"/api/v1/posts/?size={size}&page={page+1}" \
            + f"&postid_lte={postid_lte}"
    else:
        next_u = ""
    # recover the url with parameters
    url = '/api/v1/posts/?'
    for arg in request.args:
        url = url + arg + '=' + request.args[arg] + '&'
    url = url[:len(url) - 1]
    context = {'results': posts, 'next': next_u, 'url': url}
    return jsonify(**context)


@insta485.app.route('/api/v1/posts/<int:postid>/', methods=['GET'])
@check_auth
def get_single_post(postid):
    """Return the details for one post."""
    logname = session['logname']
    connection = insta485.model.get_db()
    context = connection.execute(
        'SELECT * FROM posts WHERE postid = ?', (postid,)
    ).fetchone()
    if context is None:
        raise InvalidUsage('Post not found', status_code=404)
    # comments (commentid@, lognameOwnsThis, owner@, ownerShowUrl, text@, url)
    comments = connection.execute(
        'SELECT * FROM comments WHERE postid = ? '
        'ORDER BY commentid', (postid,)
    ).fetchall()
    for comment in comments:
        comment['lognameOwnsThis'] = comment['owner'] == logname
        comment['ownerShowUrl'] = f"/users/{comment['owner']}/"
        comment['url'] = f"/api/v1/comments/{comment['commentid']}/"
        del comment['created']
        del comment['postid']
    context['comments'] = comments
    # comments_url
    context['comments_url'] = f"/api/v1/comments/?postid={postid}"
    # created@
    # imgUrl
    context['imgUrl'] = '/uploads/' + context['filename']
    del context['filename']
    # likes (lognameLikesThis, numLikes, url)
    likes = {}
    likeid = connection.execute(
        'SELECT likeid FROM likes WHERE postid = ? and owner = ?',
        (postid, logname)
    ).fetchone()
    if likeid is None:
        likes['lognameLikesThis'] = False
        likes['url'] = None
    else:
        likes['lognameLikesThis'] = True
        likes['url'] = f"/api/v1/likes/{likeid['likeid']}/"
    likes['numLikes'] = connection.execute(
        'SELECT COUNT(*) FROM likes WHERE postid = ?', (postid,)
    ).fetchone()['COUNT(*)']
    context['likes'] = likes
    # owner@
    # ownerImgUrl
    context['ownerImgUrl'] = '/uploads/' + connection.execute(
        'SELECT filename FROM users WHERE username = ?',
        (context['owner'],)
    ).fetchone()['filename']
    # ownerShowUrl
    context['ownerShowUrl'] = f"/users/{context['owner']}/"
    # postShowUrl
    context['postShowUrl'] = f"/posts/{context['postid']}/"
    # postid@
    # url
    context['url'] = f"/api/v1/posts/{context['postid']}/"
    return flask.jsonify(**context)
