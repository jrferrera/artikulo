from artikulo import app
from artikulo.artikulo import Home

app.add_url_rule('/', 'home', Home().index)