from artikulo import app
from profile.profile import Profile

app.add_url_rule('/view_profile', 'view_profile', Profile().show, methods = ['GET'])