from artikulo import login_manager
from registration.models import User

@login_manager.user_loader
def load_user(id):
	return User.query.get(int(id))