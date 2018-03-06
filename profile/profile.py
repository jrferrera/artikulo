from flask import Flask, Blueprint, render_template
from flask_login import current_user, login_required

profile = Blueprint('profile', __name__, template_folder = 'templates')

class Profile:
	@login_required
	def show(self):
		return render_template('profiles/show.html', title = 'Profile')