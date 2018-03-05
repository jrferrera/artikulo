from flask import render_template
from artikulo import app

from flask_login import login_required

class Home:
	@login_required
	def index(self):
		return render_template('home/index.html', title = 'Home')