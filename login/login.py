from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from flask_login import current_user, login_user, logout_user
from login.forms import LoginForm, ResetPasswordRequestForm, ResetPasswordForm
from registration.models import User

from artikulo import app
from artikulo.email import send_email, send_password_reset_email

from flask_babel import _

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
				flash(_('Invalid username or password.'))
				return redirect(url_for('login'))
			
			login_user(user, remember = login_form.remember_me.data)
			flash('Successfully logged in.')
			return redirect(url_for('home'))

		return render_template('sessions/new.html', title = 'Log In', login_form = login_form)

	def destroy(self):
		logout_user()
		return redirect(url_for('home'))


class Password:
	def new(self):
		if current_user.is_authenticated:
			return redirect(url_for('home'))
		
		reset_password_form = ResetPasswordRequestForm()
		
		if reset_password_form.validate_on_submit():
			user = User.query.filter_by(email = reset_password_form.email.data).first()
			
			if user:
				send_password_reset_email(user)
				flash('Check your email for the instructions to reset your password')
				return redirect(url_for('login'))
		
		return render_template('passwords/reset.html', title = 'Reset Password', reset_password_form = reset_password_form)
	
	def send_password_reset_email(self, user):
		token = user.get_reset_password_token()
		send_email('[Artikulo] Reset Your Password',
							sender = app.config['ADMINS'][0],
							recipients = [user.email],
							text_body = render_template('emails/reset_password_request.txt', user = user, token = token),
							html_body = render_template('emails/reset_password_request.html', user = user, token = token))

	def reset_password(self, token):
		if current_user.is_authenticated:
			return redirect(url_for('index'))
		
		user = User.verify_reset_password_token(token)
		print(user)

		if not user:
			return redirect(url_for('login'))
			
		reset_password_form = ResetPasswordForm()
		
		if reset_password_form.validate_on_submit():
			print(user)
			user.set_password(reset_password_form.password.data)
			user.save()
			flash('Your password has been reset.')
			return redirect(url_for('login'))
		
		return render_template('passwords/reset_password.html', user = user, reset_password_form = reset_password_form)