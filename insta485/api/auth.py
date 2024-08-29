"""REST API auth and error handler."""
from functools import wraps
from flask import jsonify, request, session
import insta485
from insta485.views.account import verify_password


class InvalidUsage(Exception):
    """Basic http exception class."""

    status_code = 400

    def __init__(self, message, status_code=None, payload=None):
        """Create exception."""
        Exception.__init__(self)
        self.message = message
        if status_code is not None:
            self.status_code = status_code
        self.payload = payload

    def to_dict(self):
        """Make to dict."""
        retval = dict(self.payload or ())
        retval['message'] = self.message
        return retval


@insta485.app.errorhandler(InvalidUsage)
def handle_invalid_usage(error):
    """Handle exceptions."""
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


def authenticate():
    """Authenticate when necessary.

    Access by either logged in or providing authorization.
    """
    if 'logname' in session:
        return
    if request.authorization is None:
        raise InvalidUsage('Forbidden', status_code=403)
    username = request.authorization['username']
    password = request.authorization['password']
    if not username or not password:
        raise InvalidUsage('Forbidden', status_code=403)
    connection = insta485.model.get_db()
    password_db = connection.execute(
        'SELECT password FROM users WHERE username = ?', (username,)
    ).fetchone()
    if password_db is None:
        raise InvalidUsage('Forbidden', status_code=403)
    password_db = password_db['password']
    if not verify_password(password, password_db):
        raise InvalidUsage('Forbidden', status_code=403)
    # login user with authorization
    session['logname'] = username


def check_auth(func):
    """Check authentication before calling function."""
    @wraps(func)
    def decorated(*args, **kwargs):
        authenticate()
        return func(*args, **kwargs)
    return decorated
