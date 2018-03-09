from flask import Flask, Blueprint, url_for, redirect, flash, render_template, request
from posts.forms import ArticleForm
from posts.models import Article
from registration.models import User

from artikulo import app

from flask_login import login_required, current_user

post = Blueprint('post', __name__, template_folder = 'templates')

class Post:
	@login_required
	def index(self):
		page = request.args.get('page', 1, type = int)
		articles = current_user.articles.order_by('updated_at desc').paginate(page, app.config['POSTS_PER_PAGE'], False)
		next_url = url_for('my_articles', page = articles.next_num) if articles.has_next else None
		previous_url = url_for('my_articles', page = articles.prev_num) if articles.has_prev else None
		return render_template('articles/index.html', title = 'My Articles', articles = articles.items, next_url = next_url, previous_url = previous_url)
		
	@login_required
	def show(self, id):
		article = Article.query.get(id)
		return render_template('articles/show.html', title = article.title, article = article)

	@login_required
	def new(self):
		article_form = ArticleForm()
		return render_template('articles/new.html', title = 'Create Post', article_form = article_form)

	@login_required
	def create(self):
		article_form = ArticleForm()

		if article_form.validate_on_submit():
			article = Article(author = current_user, title = article_form.title.data, content = article_form.content.data)
			article.save()
			flash('Successfully posted an article.')
			return redirect(url_for('show_post', id = article.id))
			