import os
from flask import Flask
from flask_bootstrap import Bootstrap
from flask_mail import Mail
from flask_moment import Moment
from flask_sqlalchemy import SQLAlchemy
from config import config

bootstrap = Bootstrap()
mail = Mail()
moment = Moment()
db = SQLAlchemy()


def create_app(config_name):
    print(__name__)
    app = Flask(__name__)
    app.config.from_object(config[config_name])
    print(config[config_name])
    config[config_name].init_app(app)

    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .views.home import home as main_blueprint
    app.register_blueprint(main_blueprint)

    print(app.url_map)
    return app
