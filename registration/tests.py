from datetime import datetime, timedelta
import unittest
from artikulo import app, db
from registration.models import User
from posts.models import Article
import os

class UserModelCase(unittest.TestCase):
  def setUp(self):
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@127.0.0.1:3306/artikulo_test'
    db.create_all()
		
  def tearDown(self):
    db.session.remove()
    db.drop_all()

  def test_password_hashing(self):
    user = User(username = 'juan')
    user.set_password('password')
    self.assertFalse(user.check_password('pwd'))
    self.assertTrue(user.check_password('password'))

  def test_avatar(self):
    user = User(username = 'john', email = 'john@example.com')
    self.assertEqual(user.avatar(128), ('https://www.gravatar.com/avatar/d4c74594d841139328695756648b6bd6?d=identicon&s=128'))
