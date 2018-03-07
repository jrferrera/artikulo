from artikulo import app
from posts.post import Post

app.add_url_rule('/my_articles', 'my_articles', Post().index, methods = ['GET'])
app.add_url_rule('/posts', 'new_post', Post().new, methods = ['GET'])
app.add_url_rule('/posts/<id>', 'show_post', Post().show, methods = ['GET'])
app.add_url_rule('/posts', 'create_post', Post().create, methods = ['POST'])