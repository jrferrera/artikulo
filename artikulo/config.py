import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY')

	if os.environ.get('DATABASE_URI'):
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
	else:
		SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1/artikulo_development'
	
	SQLALCHEMY_TRACK_MODIFICATIONS = False