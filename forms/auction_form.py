from wtforms.fields import StringField, SelectField, IntegerField, TimeField
from flask_wtf import FlaskForm
from flask_wtf.file import FileRequired, FileField
from wtforms.validators import DataRequired, InputRequired
from .choices import choices

class AuctionForm(FlaskForm):
    name = StringField('name of the auction', validators=[DataRequired()])
    category = SelectField('Category', choices=choices)
    city = StringField("City", validators=[DataRequired()])
    minimal_price = IntegerField("Minimum price")
    auction_image = FileField("Auction image", validators=[FileRequired()])
    end_date = StringField("End date", validators=[InputRequired()])
    end_time = TimeField("End time", validators=[InputRequired()])
    description = StringField("Description", validators=[DataRequired()])