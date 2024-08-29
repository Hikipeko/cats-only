"""
Insta485 get static files.

URLs include:
/uploads/
/images/
/css/
"""

import flask
import insta485


@insta485.app.route("/uploads/<filename>", methods=["GET"])
def send_image(filename):
    """Send image from filesystem."""
    if 'logname' not in flask.session:
        flask.abort(403)
    return flask.send_from_directory(
        insta485.app.config["UPLOAD_FOLDER"], filename)


@insta485.app.route("/images/<filename>", methods=["GET"])
def send_static_image(filename):
    """Send image from filesystem."""
    return flask.send_from_directory(
        insta485.app.config["IMAGES_FOLDER"], filename)


@insta485.app.route("/css/<filename>", methods=["GET"])
def send_static_css(filename):
    """Send image from filesystem."""
    return flask.send_from_directory(
        insta485.app.config["CSS_FOLDER"], filename)


@insta485.app.route("/favicon.ico", methods=["GET"])
def send_favicon():
    """Send image from filesystem."""
    return flask.send_from_directory(
        insta485.app.config["STATIC_FOLDER"], "favicon.ico")
