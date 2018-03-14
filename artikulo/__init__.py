from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from artikulo.config import Config

import logging
from logging.handlers import SMTPHandler
from logging.handlers import RotatingFileHandler
import os
from flask_mail import Mail

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)
mail = Mail(app)

from flask_assets import Environment, Bundle

bundles = {
  'general_css' : Bundle('styles/layouts.css', 'styles/registrations.css', output = 'general/layouts.css'),
  'general_js' : Bundle('scripts/lib/jquery-3.3.1.min.js', 'scripts/layouts.js', output = 'general/layouts.js')
}

assets = Environment(app)
assets.register(bundles)

from flask_login import LoginManager, current_user
from datetime import datetime

login_manager = LoginManager(app)
login_manager.login_view = 'login'
from login.models import load_user

from artikulo import routes, errors
from registration.registration import registration
from registration import models
from registration.models import User, Profile

app.register_blueprint(registration)

from login.login import login
app.register_blueprint(login)

from profile.profile import profile
app.register_blueprint(profile)

from posts.models import Article

from posts.post import post
app.register_blueprint(post)

if not app.debug:
  if app.config['MAIL_SERVER']:
    auth = None
    
    if app.config['MAIL_USERNAME'] or app.config['MAIL_PASSWORD']:
      auth = (app.config['MAIL_USERNAME'], app.config['MAIL_PASSWORD'])
      secure = None
      
      if app.config['MAIL_USE_TLS']:
        secure = ()
        mail_handler = SMTPHandler(
          mailhost = (app.config['MAIL_SERVER'], app.config['MAIL_PORT']),
          fromaddr = 'no-reply@' + app.config['MAIL_SERVER'],
          toaddrs = app.config['ADMINS'], subject = 'Artikulo Errors',
          credentials = auth,
          secure = secure
        )
        
        mail_handler.setLevel(logging.ERROR)
        app.logger.addHandler(mail_handler)
  if not os.path.exists('logs'):
    os.mkdir('logs')
  filename = 'artikulo-' + datetime.utcnow().strftime('%Y-%m-%d') + '.log'
  file_handler = RotatingFileHandler('logs/' + filename, maxBytes = 10240, backupCount = 10)
  file_handler.setFormatter(logging.Formatter('%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'))
  file_handler.setLevel(logging.INFO)
  app.logger.addHandler(file_handler)
  app.logger.setLevel(logging.INFO)
  app.logger.info('Artikulo Startup')


@app.before_request
def before_request():
	if current_user.is_authenticated:
		current_user.last_login = datetime.utcnow()
		current_user.save()

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Profile': Profile}