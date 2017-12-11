from flask.ext.login import LoginManager
from app import app

login_manager = LoginManager()
login_manager.setup_app(app)