import logging
import os
from flask import Blueprint, send_file, jsonify

from ..config import BASEDIR


log = logging.getLogger(__name__)
code = Blueprint("code", __name__, url_prefix="/code")


@code.route("/")
def code_text():
    return jsonify(open(os.path.join(BASEDIR, "data", "tracker.py"), "r", encoding="utf-8").read())

@code.route("/download")
def download():
    return send_file(os.path.join(BASEDIR, "data", "tracker.py"), as_attachment=True)