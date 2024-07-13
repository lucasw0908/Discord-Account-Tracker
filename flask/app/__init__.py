import logging
import logging.handlers
import os
from flask import Flask
from flask.logging import default_handler
from flask_wtf import CSRFProtect

from .config import DevConfig, ProdConfig, BASEDIR
from .models import db
from .modules.bot import bot
from .modules.socketio import socketio


log = logging.getLogger(__name__)


def init_logger(debug: bool=False) -> None:
    """
    Parameters
    ----------
    debug: :type:`bool`
        If debug is true, the logger will log all messages.
    """
        
    formatter = logging.Formatter("[{asctime}] {levelname} {name}: {message}", datefmt="%Y-%m-%d %H:%M:%S", style="{")
    
    if debug:
        log.setLevel(logging.DEBUG)
    else:
        log.setLevel(logging.INFO)
        
    file_handler = logging.handlers.RotatingFileHandler(
        filename=os.path.join(BASEDIR, "app.log"),
        encoding="utf-8",
        maxBytes=8**7, 
        backupCount=8
    )
        
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)
    logging.getLogger().addHandler(file_handler)
    
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)
    logging.getLogger().addHandler(console_handler)
    
    #logging.getLogger().addHandler(default_handler)
    
def app_load_blueprints(app: Flask) -> None:
    """
    Load all blueprints
    
    Parameters
    ----------
    app: :class:`Flask`
        The flask app.
    """
    
    from .views.account_sys import account_sys
    from .views.code import code
    from .views.error_handler import error_handler
    from .views.main import main
    
    app.register_blueprint(account_sys)
    app.register_blueprint(code)
    app.register_blueprint(error_handler)
    app.register_blueprint(main)
    
    
def create_app() -> Flask:
    """
    Returns
    -------
    app: :class:`Flask`
        A flask app.
    """
    init_logger()
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    csrf = CSRFProtect(app)
    db.__init__(app)
    socketio.init_app(app)
    with app.app_context(): db.create_all()
    app_load_blueprints(app)
    bot.run_thread()
    
    return app