from app import db
from app import app

# Create our database model
class User(db.Model):
    __tablename__ = "users"
    user_id = db.Column(db.Integer, primary_key=True)
    user_email = db.Column(db.String(120))
    user_realname = db.Column(db.String(120))
    user_password = db.Column(db.String(120))

    def __init__(self, user_email, user_realname, user_password):
        self.user_email = user_email
        self.user_realname = user_realname
        self.user_password = user_password
