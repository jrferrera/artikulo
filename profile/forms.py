from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired, Length, ValidationError

from registration.models import User
from flask_login import current_user

class EditProfileForm(FlaskForm):
	username = StringField('Username', validators=[DataRequired()])
	about_me = TextAreaField('About Me', validators=[Length(min = 0, max = 140)])
	submit = SubmitField('Submit')

	def validate_username(self, username):
		if current_user.username != username.data:
			user = User.query.filter_by(username = username.data).first()
			if user is not None: 
				raise ValidationError('Username already exists.')