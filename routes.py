from flask.globals import request
from flask.helpers import url_for
from flask_migrate import current
from app import app, db
from flask import render_template, flash, redirect, request
from forms import LoginForm, RegisterForm
from flask_login import current_user, login_user, logout_user, login_required
from models import User
from werkzeug.urls import url_parse


import articles
app.register_blueprint(articles.bp)

@app.route('/')
@app.route('/index')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user is None or not user.check_password(form.password.data):
            flash('Invalid username or password.')
            return redirect(url_for('login'))
        login_user(user, remember=form.remember_me.data)
        # If page requires login, checks and redirect accordingly
        next_page = request.args.get('next')
        if not next_page or url_parse(next_page).netloc != '':
            next_page = url_for('index')
        return redirect(next_page)
    return render_template('login.html', form=form)

@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('index'))
    form = RegisterForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You are now registered.')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)
