from . import db


class Offer(db.Model):
    __tablename__ = "Offer"
    id = db.Column(db.Integer, primary_key=True)
    auction_id = db.Column(db.Integer, db.ForeignKey('Auction.id'), nullable=False)
    user_id = db.Column(db.String(70), nullable=False)
    price = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"Offer {id}"
