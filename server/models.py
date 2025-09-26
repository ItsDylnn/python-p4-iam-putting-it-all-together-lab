from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

class User(db.Model):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    _password_hash = db.Column("password", db.String(128), nullable=False)
    # add other fields if needed
    bio = db.Column(db.String(200))
    image_url = db.Column(db.String(200))

    # Password setter
    def set_password(self, password):
        self._password_hash = generate_password_hash(password)

    # Password checker
    def check_password(self, password):
        return check_password_hash(self._password_hash, password)

class Recipe(db.Model):
    __tablename__ = "recipes"
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    instructions = db.Column(db.Text, nullable=False)
    minutes_to_complete = db.Column(db.Integer)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"))
