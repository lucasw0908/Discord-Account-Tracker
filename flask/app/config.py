from dotenv import load_dotenv
import os
from datetime import timedelta


BASEDIR = os.path.abspath(os.path.dirname(__file__))
load_dotenv(os.path.join(BASEDIR, ".env"), override=True)

TOKEN = os.getenv("TOKEN")
CLIENT_ID = os.getenv("CLIENT_ID")
CLIENT_SECRET = os.getenv("CLIENT_SECRET")
REDIRECT_URI = os.getenv("REDIRECT_URI")
SQLALCHEMY_DATABASE_URI = os.getenv("SQLALCHEMY_DATABASE_URI")
ADMIN_ID = int(os.getenv("ADMIN_ID"))
OAUTH_URL = "https://discord.com/oauth2/authorize?client_id=" + CLIENT_ID + "&redirect_uri=" + REDIRECT_URI + "&response_type=code&scope=identify+email" 


class Config(object):
    SECRET_KEY = os.urandom(12).hex()
    JSON_AS_ASCII = False
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PERMANENT_SESSION_LIFETIME = timedelta(days=31)


class ProdConfig(Config):
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = SQLALCHEMY_DATABASE_URI


class DevConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASEDIR, "db.sqlite3")