from . import db


class Users(db.Model):
    __tablename__ = "users"
    
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(32), unique=True, nullable=False)
    userid = db.Column(db.Integer, unique=True, nullable=False)
    token = db.Column(db.String(64), unique=True, nullable=False)
    url = db.Column(db.String(128), unique=True, nullable=False)
    avatar = db.Column(db.String(128), nullable=False)
    flags = db.Column(db.PickleType(), nullable=False)
    created_at = db.Column(db.String(32), nullable=False, default=db.func.now())
    is_admin = db.Column(db.String(128), default=False)
    
    
    def __init__(self, username: str, id: int, token: str, avatar: str, url: str, flags: list, created_at: str) -> None:
        self.username = username
        self.userid = id
        self.token = token
        self.avatar = avatar
        self.url = url
        self.flags = flags
        self.created_at = created_at
        
    
    def __repr__(self):
        return f"<User {self.username}>"