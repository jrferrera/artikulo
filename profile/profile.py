from flask import Flask, Blueprint, render_template
from flask_login import current_user, login_required
from registration.models import User

profile = Blueprint('profile', __name__, template_folder = 'templates')

class Profile:
	@login_required
	def show(self, username):
		user = User.query.filter_by(username = username).first_or_404()
		return render_template('profiles/show.html', title = 'Profile', user = user)