from flask import Flask, Blueprint, render_template, url_for, redirect
from registration.forms import RegistrationForm

registration = Blueprint('registration', __name__, template_folder = 'templates')

class Registration:
	def new(self):
		registration_form = RegistrationForm()
		return render_template('registrations/new.html', title = 'Register', registration_form = registration_form)
	
	def create(self):
		registration_form = RegistrationForm()
		
		if registration_form.validate_on_submit():
			return redirect(url_for('home'))
		return render_template('registrations/new.html', title = 'Register', registration_form = registration_form)