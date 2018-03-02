from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from artikulo.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from artikulo import routes
from registration.registration import registration
from registration import models
from registration.models import User, Profile

app.register_blueprint(registration)

@app.shell_context_processor
def make_shell_context():
	return {'db': db, 'User': User, 'Profile': Profile}