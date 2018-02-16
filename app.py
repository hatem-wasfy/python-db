# Imports

import os
from urllib import parse
import psycopg2
from flask import Flask
from flask import request
from flask import make_response


app = Flask(__name__)
#parse.uses_netloc.append("postgres")
#url = parse.urlparse(os.environ["postgres://swkjnmiksbabsb:c9a348935037d022f6450c7deb6df6ad9d846d736bf04c44b52338092f046554@ec2-174-129-221-240.compute-1.amazonaws.com:5432/d50jsgearpigne"])

conn = psycopg2.connect(
    database="d50jsgearpigne",
    user="swkjnmiksbabsb",
    password="c9a348935037d022f6450c7deb6df6ad9d846d736bf04c44b52338092f046554",
    host="ec2-174-129-221-240.compute-1.amazonaws.com",
    port=5432
)




# Config

##app = Flask(__name__)
##db = SQLAlchemy(app)
##app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres:///swkjnmiksbabsb:c9a348935037d022f6450c7deb6df6ad9d846d736bf04c44b52338092f046554@ec2-174-129-221-240.compute-1.amazonaws.com:5432/d50jsgearpigne'
##SALT = 'Hashids SALT'


##class Url(db.Model):

    # Create table `urls` |id|url|

    ##__tablename__ = "urls"
    ##id = db.Column(db.Integer, primary_key=True) 
    ##url = db.Column(db.Text)

    ##def __init__(self, url):
        ##self.url = url
        
        
##if __name__ == '__main__':
    ##app.run(debug=True)

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
    
