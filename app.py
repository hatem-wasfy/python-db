from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
import sys
import json
from flask_heroku import Heroku

from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['postgres://yrkgfdwphwaktc:c5b75242c71781f8dbdb1df56f91ae89cc291dcbeb54fd88d3b543ebf5b4a207@ec2-107-22-175-33.compute-1.amazonaws.com:5432/def7m51jhsgoca
'] = os.environ['ec2-107-22-175-33.compute-1.amazonaws.com']
db = SQLAlchemy(app)
