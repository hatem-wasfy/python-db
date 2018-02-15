from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
db = SQLAlchemy(app)
