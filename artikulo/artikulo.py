from flask import render_template
from artikulo import app

from flask_login import login_required
from posts.models import Article
from posts.forms import ArticleForm

class Home:
	@login_required
	def index(self):
		articles = Article.query.all()
		return render_template('home/index.html', title = 'Home', articles = articles)