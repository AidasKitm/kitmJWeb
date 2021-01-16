from forms.auction_form import AuctionForm
from flask import request, render_template, redirect, url_for, session
from models.user import User
from models.auction import Auction
from werkzeug import secure_filename
from app import app
from datetime import datetime
from models import db

@app.route('/create_auction', methods=["GET", "POST"])
def create_auction():
    if request.method == "GET":
        form = AuctionForm()
        if session.get('user') is None:
            return redirect(url_for('register'))
        return render_template('create_auction.html', form=form)
    else:
        form = AuctionForm()
        end_day = datetime.strptime(form.end_date, '%d-%m-%Y')
        if form.validate_on_submit():
            user = User.query.filter(email=session.get('user')).first()
            image = form.auction_image.data
            image_name = user.email + "__" + image.filename
            image_name = secure_filename(image_name)

        new_auction = Auction(name=form.name, category=form.category, description=form.description, city=form.city,
                              minimal_price=form.minimal_price, auction_image=image_name, end_date=end_day,
                              end_time=form.end_time, user_id= user.id)
        db.session.add(new_auction)
        db.session.commit()
        return redirect(url_for('auction', auction_id=Auction.query.order(Auction.id.desc()).first().id))
