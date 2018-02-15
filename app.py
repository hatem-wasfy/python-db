# Imports

from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
#from hashids import Hashids

# Config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///yrkgfdwphwaktc:c5b75242c71781f8dbdb1df56f91ae89cc291dcbeb54fd88d3b543ebf5b4a207@ec2-107-22-175-33.compute-1.amazonaws.com:5432/def7m51jhsgoca'
SALT = 'Hashids SALT'


class Url(db.Model):

    # Create table `urls` |id|url|

    __tablename__ = "urls"
    id = db.Column(db.Integer, primary_key=True) 
    url = db.Column(db.Text)

    def __init__(self, url):
        self.url = url
        
        
if __name__ == '__main__':
    app.run(debug=True)
    
