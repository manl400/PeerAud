from app import db
from app import app

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(120))
    user_username = db.Column(db.String(120))
    user_password = db.Column(db.String(120))

    def __init__(self, user_name, user_username, user_password):
        self.user_name = user_name
        self.user_username = user_username
        self.user_password = user_password
