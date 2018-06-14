from flask import Flask
from .config import DevConfig
from flask_bootstrap import Bootstrap

# initialising the application
app = Flask(__name__, instance_relative_config = True)

# setting up configuration
app.config.from_object(DevConfig)
app.config.from_pyfile('config.py')

# initialising flask extensions
bootstrap = Bootstrap(app)
from app import views

#registering the model blueprint
# from models import models as models_blueprint
# app.register_blueprint(models_blueprint)