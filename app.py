# Imports

from flask import Flask, redirect, request, render_template
from flask_sqlalchemy import SQLAlchemy
from hashids import Hashids

# Config

app = Flask(__name__)
db = SQLAlchemy(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'
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
    
