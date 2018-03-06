from artikulo import app
from login.login import Session

app.add_url_rule('/login', 'login', Session().new, methods = ['GET'])
app.add_url_rule('/login', 'signin', Session().create, methods = ['POST'])
app.add_url_rule('/logout', 'logout', Session().destroy, methods = ['GET'])