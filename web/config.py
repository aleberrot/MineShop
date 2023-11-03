import os
basedir: str = os.path.abspath(os.path.dirname(__file__))

DB_NAME = 'app.db'

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'super-secret'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(basedir, f'{DB_NAME}')
    SQLALCHEMY_TRACK_MODIFICATIONS = False