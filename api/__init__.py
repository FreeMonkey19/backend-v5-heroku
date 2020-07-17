from flask import Flask
from flask_cors import CORS, cross_origin
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import flask_login
from flask import Response
import create_app from App
import .app from app


# instantiate db object
db = SQLAlchemy()
app = create_app()
