from datetime import datetime
from artikulo import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

from artikulo.models import BaseModel

class User(BaseModel, UserMixin, db.Model):
  __tablename__ = 'users'

  email = db.Column(db.String(255), index = True, unique = True, nullable = False)
  password_hash = db.Column(db.String(255), nullable = False)
  profile = db.relationship('Profile', backref = 'user')

  def __repr__(self):
    return '<User {}>'.format(self.email)
  
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Profile(BaseModel, db.Model):
  __tablename__ = 'profiles'

  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  first_name = db.Column(db.String(255), index = True, nullable = False)
  last_name = db.Column(db.String(255), index = True, nullable = False)
  
  def __repr__(self):
    return '<Profile {}>'.format(self.first_name)