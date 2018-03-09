import os

class Config(object):
	SECRET_KEY = os.environ.get('SECRET_KEY')

	if os.environ.get('DATABASE_URI'):
		SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URI')
	else:
		SQLALCHEMY_DATABASE_URI = 'mysql://root:root@127.0.0.1:3306/artikulo_development'
	
	SQLALCHEMY_TRACK_MODIFICATIONS = False

	POSTS_PER_PAGE = 3

	MAIL_SERVER = os.environ.get('MAIL_SERVER')
	MAIL_PORT = int(os.environ.get('MAIL_PORT') or 25)
	MAIL_USE_TLS = os.environ.get('MAIL_USE_TLS') is not None
	MAIL_USERNAME = os.environ.get('MAIL_USERNAME')
	MAIL_PASSWORD = os.environ.get('MAIL_PASSWORD')
	ADMINS = ['your-email@example.com']