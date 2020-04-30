from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from f.config import Config
db = SQLAlchemy()
bcrypt = Bcrypt()
login_manager = LoginManager()
login_manager.login_view = 'users.login'
def create_app(config_class=Config): ## funtion to create flask app 
	app = Flask(__name__)
	app.config['SECRET_KEY']=Config.SECRET_KEY
	app.config['SQLALCHEMY_DATABASE_URI']=Config.SQLALCHEMY_DATABASE_URI
	db.init_app(app)
	bcrypt.init_app(app)
	login_manager.init_app(app) 
	from f.users.routes import users  
	from f.main.routes import main
	app.register_blueprint(users) ## blue prints from the users 
	app.register_blueprint(main) ##blue prints from the main
	return app