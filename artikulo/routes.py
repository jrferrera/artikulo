from artikulo import app
from artikulo.artikulo import Home
from registration.registration import Registration
from login.login import Session

from registration import routes
from login import routes
from profile import routes
from posts import routes

app.add_url_rule('/', 'home', Home().index)