import os
import json

from ..config import BASEDIR
from .bot import bot
from ..models import db
from ..models.users import Users


def get_data_from_json() -> list:
    """Get all the data from the users.json file."""
    with open(os.path.join(BASEDIR, "data", "users.json"), "r", encoding="utf-8") as file:
        return json.load(file)
    

def save_data_to_json(data: dict) -> list:
    """Save the data to the users.json file."""
    data = bot.load_data(data)
    with open(os.path.join(BASEDIR, "data", "users.json"), "r+", encoding="utf-8") as file:
        file_data: list = json.load(file)
        if data not in file_data: file_data.append(data)
        file.seek(0)
        json.dump(file_data, file, indent=4)
        return file_data
    
    
def get_data() -> list:
    """Get all the data from the database."""
    db.create_all()
    return Users.query.all()
    
    
def save_data(data: dict) -> list:
    """Save the data to the database."""
    db.create_all()
    if Users.query.filter_by(token=data["token"]).all():
        return Users.query.filter_by(token=data["token"]).all()[0]
    data = bot.load_data(data)
    user = Users(**data)
    db.session.add(user)
    db.session.commit()
    return user