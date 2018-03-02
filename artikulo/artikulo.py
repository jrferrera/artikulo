from flask import render_template
from artikulo import app

class Home:
	def index(self):
		return render_template('home/index.html', title = 'Home')