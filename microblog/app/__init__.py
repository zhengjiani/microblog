from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_login import LoginManager
<<<<<<< HEAD
from flask_mail import Mail
from flask_bootstrap import Bootstrap
=======
>>>>>>> cb42cf1161480375b2e587f432535d5c4f2c0e80
app=Flask(__name__)
app.config.from_object(Config)
db=SQLAlchemy(app)
migrate = Migrate(app,db)
<<<<<<< HEAD
mail=Mail(app)
bootstrap=Bootstrap(app)
=======
>>>>>>> cb42cf1161480375b2e587f432535d5c4f2c0e80
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view='login'
from app import routes,models,errors



