from app import db


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(70), unique=True, nullable=False)
    password = db.Column(db.String(50), nullable=True)
    address = db.Column(db.String(80), nullable=False)
    profile_image = db.Column(db.String(256), nullable=True, default="default.jpg")
    auction = db.relationship("Auction", backref='user', lazy=True)
