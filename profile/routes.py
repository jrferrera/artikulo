from artikulo import app
from profile.profile import Profile

app.add_url_rule('/profile/<username>', 'show_profile', Profile().show, methods = ['GET'])
app.add_url_rule('/profile/edit_my_profile', 'edit_my_profile', Profile().edit_my_profile, methods = ['GET', 'POST'])