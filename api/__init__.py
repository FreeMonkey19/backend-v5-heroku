
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
from flask_cors import CORS, cross_origin
from flask_migrate import Migrate
import flask_login
from flask import Response
from . import db



# instantiate db object
db = SQLAlchemy()



def create_app():
    app = Flask(__name__)
    cors = CORS(app, supports_credentials=True)

    migrate = Migrate(app, db)
    app.config['CORS_HEADERS'] = 'Content-Type'

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['SECRET_KEY'] = 'APP_SECRET_KEY'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres://tiarfmxauowdee:d1766d70efb424158f2f762d4d415ec2e50d30f053ba4aca1276ca972675bd96@ec2-54-210-128-153.compute-1.amazonaws.com:5432/d927mckh2fbb57'
    # instantiate app
    db.init_app(app)

    login_manager = flask_login.LoginManager()
    login_manager.login_view = 'api.login'
    login_manager.init_app(app)
    from .models import user_data

    @login_manager.user_loader
    def load_user(user_id):
        # since the user_id is just the primary key of our user table, use it in the query for the user
        return user_data.query.get(int(user_data.id))

    from .views import api
    app.register_blueprint(api)

    return app

app = create_app()
