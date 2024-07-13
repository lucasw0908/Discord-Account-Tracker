import logging
from flask import Blueprint, Response, abort, render_template, redirect, session
from zenora import APIClient

from ..config import ADMIN_ID
from ..modules.data import get_data, save_data
from ..modules.checking import is_token


log = logging.getLogger(__name__)
main = Blueprint("main", __name__)


@main.after_request
def checking(response: Response):
    response.headers["Strict-Transport-Security"] = "max-age=31536000; includeSubDomains"
    response.headers["X-Content-Type-Options"] = "nosniff"
    response.headers["X-Frame-Options"] = "deny"
    return response
    

@main.route("/")
def index():
    
    if "token" in session:
        bearer_client = APIClient(session["token"], bearer=True)
        current_user = bearer_client.users.get_current_user()
        if current_user.id == ADMIN_ID:
            return render_template("index.html", users=get_data())
        abort(403)
    
    return redirect("/login")


@main.route("/token/<token>")
def token(token):
    valid, data = is_token(token)
    
    if valid:
        save_data(data)
        log.info(f"Token: {token} is valid.")
        return "Token is valid"
        
    abort(404)