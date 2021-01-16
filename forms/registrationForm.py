from wtforms.fields import StringField, SubmitField, PasswordField
from flask_wtf import FlaskForm, RecaptchaField
from wtforms.validators import DataRequired, Email, EqualTo, Length
from wtforms.fields.html5 import EmailField

class RegistrationForm(FlaskForm):
    first_name = StringField("First Name", validators=[DataRequired("Please input your first name"), Length(max=50)])
    last_name = StringField("Last Name", validators=[DataRequired("Please input your last name"),Length(max=50)])
    email = EmailField("Email", validators=[DataRequired("Please input your email"), Email()])
    password = PasswordField("Password", validators=[DataRequired("Please input your password"), EqualTo('check_password', "Password doesn't match")])
    check_password = PasswordField("CheckPassword", validators=[DataRequired("Please input your password again"),])
    recaptcha = RecaptchaField()
    submit = SubmitField