from flask import Flask

app = Flask(__name__)

from artikulo import routes
from registration.registration import registration
from artikulo.config import Config

app.register_blueprint(registration)
app.config.from_object(Config)