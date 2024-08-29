"""Insta485 development configuration."""

import pathlib

# Root of this application, useful if it doesn't occupy an entire domain
APPLICATION_ROOT = '/'

# Secret key for encrypting cookies
SECRET_KEY = \
    b'\xc0\xd9\xbe]\xfe\xaeb03q^\xa5\xfb\x95\x89\x80\xf0.T\xf8\x90\xe1t%'
SESSION_COOKIE_NAME = 'login'

# File Upload to var/uploads/
INSTA485_ROOT = pathlib.Path(__file__).resolve().parent.parent
STATIC_FOLDER = INSTA485_ROOT/'insta485'/'static'
UPLOAD_FOLDER = INSTA485_ROOT/'var'/'uploads'
IMAGES_FOLDER = STATIC_FOLDER/'images'
CSS_FOLDER = STATIC_FOLDER/'css'
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])
MAX_CONTENT_LENGTH = 16 * 1024 * 1024

# Database file is var/insta485.sqlite3
DATABASE_FILENAME = INSTA485_ROOT/'var'/'insta485.sqlite3'
