from flask import request, render_template
from models.user import User
from forms.registrationForm import RegistrationForm
from werkzeug import generate_password_hash
from app import app
from models import db

@app.route('/register')
def register():
    if request.method == "GET":
        form = RegistrationForm()
        render = render_template("register.html", form=form)
    else:
        form = RegistrationForm(request.form)
        if form.validate_on_submit():
            hashed_password = generate_password_hash(form.password)
            new_user = User(first_name=form.first_name, last_name=form.last_name, email=form.email, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
        render = render_template("index.html")
    return render
