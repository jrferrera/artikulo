from artikulo import app
from profile.profile import Profile

app.add_url_rule('/profile/<username>', 'show_profile', Profile().show, methods = ['GET'])