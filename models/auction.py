from . import db
from datetime import datetime


class Auction(db.Model):
    __tablename__ = 'Auction'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=True)
    category = db.Column(db.String(50), nullable=True)
    description = db.Column(db.String(120), nullable=True)
    city = db.Column(db.String(50), nullable=True)
    minimal_price = db.Column(db.Integer, nullable=True)
    auction_image = db.Column(db.String(256), nullable=True)
    end_date = db.Column(db.Date, nullable=True, default=datetime.now())
    end_time = db.Column(db.Date, nullable=True, default=datetime.time())
    offers = db.relationship('Offer', backref='auction', lazy=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    views = db.Column(db.Integer, default=0)
