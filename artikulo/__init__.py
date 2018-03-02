from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

from artikulo.config import Config

app = Flask(__name__)
app.config.from_object(Config)
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from artikulo import routes, models
from registration.registration import registration

app.register_blueprint(registration)