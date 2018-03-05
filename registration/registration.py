from flask import Flask, Blueprint, render_template, url_for, redirect, flash
from registration.forms import RegistrationForm
from registration.models import User, Profile

registration = Blueprint('registration', __name__, template_folder = 'templates')

class Registration:
	def new(self):
		registration_form = RegistrationForm()
		return render_template('registrations/new.html', title = 'Register', registration_form = registration_form)
	
	def create(self):
		registration_form = RegistrationForm()

		if registration_form.validate_on_submit():
			user = User(email = registration_form.email.data)
			user.set_password(registration_form.password.data)
			profile = Profile(user = user, first_name = registration_form.first_name.data, last_name = registration_form.last_name.data)
			profile.save()
			flash('Successfully signed up for an account.')
			return redirect(url_for('home'))

		return render_template('registrations/new.html', title = 'Register', registration_form = registration_form)