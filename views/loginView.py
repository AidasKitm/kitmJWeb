from forms.loginForm import LoginForm
from flask import request, render_template, redirect, url_for, session
from models.user import User
from werkzeug import check_password_hash
from app import app


@app.route('/login')
def login():
    if request.method == "GET":
        form = LoginForm()
        render = render_template("Login.html", form=form)
    else:
        form = LoginForm(request.form)
        if form.validate_on_submit():
            user = User.query.filter(email=form.email.data).first()
            if user == None:
                render = redirect(url_for('login'))
            elif check_password_hash(user.password, form.password):
                session['user'] = user.email
                render = redirect(url_for('index'))
    return render