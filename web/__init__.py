from flask import Flask
from .config import Config, DB_NAME
from flask_sqlalchemy import SQLAlchemy
import os

db: SQLAlchemy = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app) 
    
    from .views import views
    from .auth import auth

    create_db(app)

    app.register_blueprint(views, url_prefix='/')
    app.register_blueprint(auth, url_prefix='/')
    return app

def create_db(app: Flask):
    if not os.path.exists(f'web/{DB_NAME}'):
        with app.app_context():
            db.create_all()
            print('Database Created!')
    else:
        print('Database already created!')