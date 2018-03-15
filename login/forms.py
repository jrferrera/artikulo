from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

from flask_babel import lazy_gettext as _l
from flask_babel import _

class LoginForm(FlaskForm):
	email = StringField(_l('Email'), validators = [DataRequired()])
	password = PasswordField(_l('Password'), validators = [DataRequired()])
	remember_me = BooleanField(_l('Remember Me'))
	submit = SubmitField(_('Sign In'))

class ResetPasswordRequestForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators = [DataRequired()])
	password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Request Password Reset')