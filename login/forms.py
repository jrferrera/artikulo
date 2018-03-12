from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class LoginForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired()])
	password = PasswordField('Password', validators = [DataRequired()])
	remember_me = BooleanField('Remember Me')
	submit = SubmitField('Sign In')

class ResetPasswordRequestForm(FlaskForm):
	email = StringField('Email', validators = [DataRequired(), Email()])
	submit = SubmitField('Request Password Reset')

class ResetPasswordForm(FlaskForm):
	password = PasswordField('Password', validators = [DataRequired()])
	password2 = PasswordField('Repeat Password', validators = [DataRequired(), EqualTo('password')])
	submit = SubmitField('Request Password Reset')