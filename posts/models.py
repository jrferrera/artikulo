from artikulo import db
from artikulo.models import BaseModel

class Article(BaseModel, db.Model):
	__tablename__ = 'articles'

	user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable = False)
	title = db.Column(db.String(255), index = True, unique = True, nullable = False)
	content = db.Column(db.Text, nullable = False)

	def __repr__(self):
		return '<Article {}>'.format(self.title)