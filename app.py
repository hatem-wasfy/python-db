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

#############******************************************

#CONNECT
conn = psycopg2.connect(
    database="d50jsgearpigne",
    user="swkjnmiksbabsb",
    password="c9a348935037d022f6450c7deb6df6ad9d846d736bf04c44b52338092f046554",
    host="ec2-174-129-221-240.compute-1.amazonaws.com",
    port=5432
)

#############******************************************




####################################################
# DELETE ALL ROWS FROM THE TABLE

curs = conn.cursor()
curs.execute("TRUNCATE TABLE japandb")
#conn.close()

####################################################



#######################################
#WRITE

city = "Fukuoka"
attraction = "food"
places = "a1 a2"
###lastchangedate = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    
###query =  "INSERT INTO japandb (city, attraction, places, lastchangedate) VALUES (%s, %s, %s, %Y-%m-%d %H:%M:%S);"
###data = (city, attraction, places, lastchangedate)

query =  "INSERT INTO japandb (city, attraction, places) VALUES (%s, %s, %s);"
data = (city, attraction, places)

curs = conn.cursor()
curs.execute(query, data)
conn.commit()


print("***************************************")

#######################################



#######################################
#READ
curs = conn.cursor()
curs.execute("SELECT * FROM japandb")
for row in curs:
    print(row)

############################################


##cur = conn.cursor()
##cur.execute(sql, (value1,value2))

##cur.close()

conn.close()


##**************************************
###get_vendors()

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
    
    ###get_vendors()

    
