from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from login.forms import LoginForm

login = Blueprint('login', __name__, template_folder = 'templates')

class Session:
	def new(self):
		login_form = LoginForm()
		return render_template('sessions/new.html', title = 'Log In', login_form = login_form)
	
	def create(self):
		login_form = LoginForm()

		if login_form.validate_on_submit():
			return redirect(url_for('home'))

		return render_template('sessions/new.html', title = 'Log In', login_form = login_form)