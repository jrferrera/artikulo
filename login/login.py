from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from login.forms import LoginForm
from registration.models import User

login = Blueprint('login', __name__, template_folder = 'templates')

class Session:
	def new(self):
		if current_user.is_authenticated:
			return redirect(url_for('home'))

		login_form = LoginForm()
		return render_template('sessions/new.html', title = 'Log In', login_form = login_form)
	
	def create(self):
		if current_user.is_authenticated:
			return redirect(url_for('home'))

		login_form = LoginForm()

		if login_form.validate_on_submit():
			user = User.query.filter_by(email = login_form.email.data).first()
			
			if user is None or not user.check_password(login_form.password.data):
				flash('Invalid username or password.')
				return redirect(url_for('login'))
			
			login_user(user, remember = login_form.remember_me.data)
			flash('Successfully logged in.')
			return redirect(url_for('home'))

		return render_template('sessions/new.html', title = 'Log In', login_form = login_form)

	def destroy(self):
		logout_user()
		return redirect(url_for('home'))