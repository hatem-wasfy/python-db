# Imports

import os
from urllib import parse
import psycopg2
from flask import Flask
from flask import request
from flask import make_response

#for google-api
import json
from googleplaces import GooglePlaces, types, lang


YOUR_API_KEY = 'AIzaSyADsZZiGIWF2laJkl5qNE5EUkSXkye4HG4'
robot_photo_url = "https://cdn.pixabay.com/photo/2014/04/03/11/55/robot-312566_960_720.png"
google_places = GooglePlaces(YOUR_API_KEY)

#########################################################



app = Flask(__name__)
#parse.uses_netloc.append("postgres")
#url = parse.urlparse(os.environ["postgres://swkjnmiksbabsb:c9a348935037d022f6450c7deb6df6ad9d846d736bf04c44b52338092f046554@ec2-174-129-221-240.compute-1.amazonaws.com:5432/d50jsgearpigne"])

###########################################################################################

#city = "Tokyo"
#attraction = "fashion"    

###query_result = google_places.nearby_search(location=city, keyword=attraction, radius=20000)




###########################################################################################




#############******************************************

#CONNECT
print("Connection to our database part")

conn = psycopg2.connect(
    database="d50jsgearpigne",
    user="swkjnmiksbabsb",
    password="c9a348935037d022f6450c7deb6df6ad9d846d736bf04c44b52338092f046554",
    host="ec2-174-129-221-240.compute-1.amazonaws.com",
    port=5432
)

#############******************************************


    

####Function to write city data from Google to our database

def insert(city, attraction, tbname, conn):
    #######################################
    #WRITE
    print("Writing row of data to our table part")

    #city = "Tokyo"
    #attraction = "fashion"
    #places = place_and_url
    #-------------------------------------------------------------
    #google query

    query_result = google_places.nearby_search(location=city, keyword=attraction, radius=20000)

    place_and_url=""
    for place in query_result.places:
        #Returned places from a query are place summaries.
        ###ok###print(place.__dict__.keys())
        ###print(place.__dict__)
        place_name = place.name
        print(place.name)
        place_geo_loc = place.geo_location
        place_id = place.place_id
        place.get_details()
        place_url=place.url
    
        #query =  "INSERT INTO japantb (city, attraction, places, url) VALUES (%s, %s, %s, %s);"
        queryline =  "INSERT INTO " + tbname + " (city, attraction, places, url) VALUES (%s, %s, %s, %s);"
        data = (city, attraction, place_name, place_url)
        curs = conn.cursor()
        curs.execute(queryline, data)
    
    
        ###global place_and_url
        ###place_and_url +="\n" + place_name + "\n" + "check it here:\n" + place_url + "\n"
        
            #place_details=place.details
            #print(place_details.__dict__.keys())
            #pf=place.photos
        print("******************************")
    conn.commit()

    #------------------------------------------------------------------------------




    ###query =  "INSERT INTO japandb (city, attraction, places) VALUES (%s, %s, %s);"
    ###data = (city, attraction, place_and_url)

    ###curs = conn.cursor()
    ###curs.execute(query, data)
    ###conn.commit()

    print("***************************************")

    #######################################
    return



    #######################################

def readtb(tbname, conn):
    #READ
    print("Reading all the rows of our table part")
    line = "SELECT * FROM " + tbname + ";"
    curs = conn.cursor()
    curs.execute(line)
    for row in curs:
        print(row)
    
    ############################################


    ##cur = conn.cursor()
    ##cur.execute(sql, (value1,value2))

    ##cur.close()

    ####conn.close()

    ##**************************************
    return


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

    




def delall(tbname, conn):
    ####################################################
    # DELETE ALL ROWS FROM THE TABLE
    print("Delete rows from our table part")

    curs = conn.cursor()
    line = "TRUNCATE TABLE " + tbname + ";"
    #curs.execute("TRUNCATE TABLE japantb;")
    curs.execute(line)
    
    #conn.close()
    return

    ####################################################
    
    
    
#------------------------------------------------------------#

#calling my functions and steps

###city = "Tokyo"
###attraction = "fashion" 
cities= ["Tokyo", "Fukuoka", "Osaka", "Kyoto"]
attractions = ["food", "shopping","souvenir", "fashion"]
tbname = "japantb"

#sending orders, for example to read city and attraction from google and write them to our database

###delall(tbname, conn)
###insert(city, attraction, tbname, conn)
###readtb(tbname, conn)

for city in cities:
    for attraction in attractions:
    words = "City: " + city + " ,attraction: " + attraction
    print(words)

    


#closing the connection to the database as the last step
conn.close()

#------------------------------------------------------------#

    
    
if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
    
    ###get_vendors()

    
