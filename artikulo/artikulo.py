from flask import render_template, request, url_for
from artikulo import app

from flask_login import login_required, current_user
from posts.models import Article
from posts.forms import ArticleForm

class Home:
	@login_required
	def index(self):
		page = request.args.get('page', 1, type = int)
		articles = Article.query.order_by('updated_at desc').paginate(page, app.config['POSTS_PER_PAGE'], False)
		next_url = url_for('home', page = articles.next_num) if articles.has_next else None
		previous_url = url_for('home', page = articles.prev_num) if articles.has_prev else None

		return render_template('home/index.html', title = 'Home', articles = articles.items, next_url = next_url, previous_url = previous_url)