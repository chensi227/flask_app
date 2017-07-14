from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
from config import config
from views import register_blueprints

# from flask_socketio import SocketIO

# socketio = SocketIO()

lm = LoginManager()
lm.session_protection = 'strong'
lm.login_view = 'admin.login'
lm.login_message = u""
app = Flask(__name__)
app.config.from_object('config')
db = SQLAlchemy()

def create_app(config_name):
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    config[config_name].init_app(app)
    register_blueprints(app)
    db.init_app(app)
    lm.init_app(app)
    # socketio.init_app(app)
    return app