from wtforms.fields import StringField, PasswordField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired, Email

class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired("Your email address"), Email])
    password = PasswordField("Password", validators=[DataRequired("Please input your password")])