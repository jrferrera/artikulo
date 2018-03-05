from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import ValidationError, DataRequired, Length, EqualTo
from registration.models import User

class RegistrationForm(FlaskForm):
  first_name = StringField('First Name', validators = [DataRequired(), Length(min = 1, max = 32)])
  last_name = StringField('Last Name', validators = [DataRequired(), Length(min = 1, max = 32)])
  email = StringField('Email', validators = [DataRequired(), Length(min = 5, max = 120)])
  password = PasswordField('Password', validators = [DataRequired(), Length(min = 6, max = 32), EqualTo('confirm_password', message = 'Passwords do not match.')])
  confirm_password = PasswordField('Confirm Password')
  submit = SubmitField('Register')

  def validate_email(self, email):
    user = User.query.filter_by(email = email.data).first()
    
    if user is not None:
      raise ValidationError('Email already exists.')