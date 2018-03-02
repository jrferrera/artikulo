from artikulo import app
from artikulo.artikulo import Home
from registration.registration import Registration

app.add_url_rule('/', 'home', Home().index)

# Registration
app.add_url_rule('/register', 'register', Registration().new, methods = ['GET'])
app.add_url_rule('/register', 'signup', Registration().create, methods = ['POST'])