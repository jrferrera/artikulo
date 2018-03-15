from flask import Flask, Blueprint, render_template, request, flash, redirect, url_for
from flask_login import current_user, login_required
from registration.models import User
from profile.forms import EditProfileForm

from flask_babel import _

profile = Blueprint('profile', __name__, template_folder = 'templates')

class Profile:
	@login_required
	def show(self, username):
		user = User.query.filter_by(username = username).first_or_404()
		return render_template('profiles/show.html', title = 'Profile', user = user)
	
	@login_required
	def edit_my_profile(self):
		edit_profile_form = EditProfileForm()

		if edit_profile_form.validate_on_submit():
			current_user.username = edit_profile_form.username.data
			current_user.about_me = edit_profile_form.about_me.data
			current_user.update()
			flash(_('You have successfully updated your profile.'))
			return redirect(url_for('edit_my_profile'))
		elif request.method == 'GET':
			edit_profile_form.username.data = current_user.username
			edit_profile_form.about_me.data = current_user.about_me
			
		return render_template('profiles/edit_my_profile.html', title = 'Edit My Profile', edit_profile_form = edit_profile_form)