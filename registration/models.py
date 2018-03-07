from datetime import datetime
from artikulo import db
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
from hashlib import md5

from artikulo.models import BaseModel
from posts.models import Article

class User(BaseModel, UserMixin, db.Model):
  __tablename__ = 'users'

  username = db.Column(db.String(255), index = True, unique = True, nullable = False)
  email = db.Column(db.String(255), index = True, unique = True, nullable = False)
  password_hash = db.Column(db.String(255), nullable = False)
  profile = db.relationship('Profile', backref = 'user')
  articles = db.relationship('Article', backref = 'author', lazy = 'dynamic')

  def __repr__(self):
    return '<User {}>'.format(self.email)
    
  def avatar(self, size = 80):
    digest = md5(self.email.lower().encode('utf-8')).hexdigest()
    return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(digest, size)

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
  
  def fullname(self):
    return self.first_name + ' ' + self.last_name