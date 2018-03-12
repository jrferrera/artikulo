from artikulo import app
from login.login import Session, Password

app.add_url_rule('/login', 'login', Session().new, methods = ['GET'])
app.add_url_rule('/login', 'signin', Session().create, methods = ['POST'])
app.add_url_rule('/logout', 'logout', Session().destroy, methods = ['GET'])
app.add_url_rule('/reset_password_request', 'reset_password_request', Password().new, methods = ['GET', 'POST'])
app.add_url_rule('/reset_password/<token>', 'reset_password', Password().reset_password, methods=['GET', 'POST'])