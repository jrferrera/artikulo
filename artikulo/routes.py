from artikulo import app
from artikulo.artikulo import Home
from registration.registration import Registration
from login.login import Session

app.add_url_rule('/', 'home', Home().index)

# Registration
app.add_url_rule('/register', 'register', Registration().new, methods = ['GET'])
app.add_url_rule('/register', 'signup', Registration().create, methods = ['POST'])

# Login
app.add_url_rule('/login', 'login', Session().new, methods = ['GET'])
app.add_url_rule('/login', 'signin', Session().create, methods = ['POST'])