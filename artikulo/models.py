from datetime import datetime
from artikulo import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
  __tablename__ = 'users'

  id = db.Column(db.Integer, primary_key = True)
  email = db.Column(db.String(255), index = True, unique = True, nullable = False)
  password_hash = db.Column(db.String(255), nullable = False)
  created_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
  updated_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
  profile = db.relationship('Profile', backref = 'user')

  def __repr__(self):
    return '<User {}>'.format(self.email)
  
  def set_password(self, password):
    self.password_hash = generate_password_hash(password)
    
  def check_password(self, password):
    return check_password_hash(self.password_hash, password)

class Profile(db.Model):
  __tablename__ = 'profiles'

  id = db.Column(db.Integer, primary_key = True)
  user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
  first_name = db.Column(db.String(255), index = True, nullable = False)
  last_name = db.Column(db.String(255), index = True, nullable = False)
  created_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
  updated_at = db.Column(db.DateTime, index = True, default = datetime.utcnow)
  
  def __repr__(self):
    return '<Profile {}>'.format(self.first_name)