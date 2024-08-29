"""Views, one for each Insta485 page."""
from insta485.views.index import show_index
from insta485.views.static_files import send_image
from insta485.views.user import show_user
from insta485.views.followers import show_followers
from insta485.views.following import show_following, edit_following
from insta485.views.post import show_post, edit_posts
from insta485.views.explore import show_explore
from insta485.views.account import show_login
from insta485.views.likes import edit_likes
from insta485.views.comments import edit_comments
