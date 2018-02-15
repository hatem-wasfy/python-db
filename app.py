#!/usr/bin/env python

import urllib
import json
import os

from flask import Flask
from flask import request
from flask import make_response

#############################
import psycopg2
#import os
#import urlparse
#from urllib.parse import urlparse
import urllib.parse
######Database########

#Python2
#urlparse.uses_netloc.append("postgres")
#url = urlparse.urlparse(os.environ["postgres://vxjbtravsqldpn:8e28f8853a5ad91bb6ec8614359773e844b6afbe8e57324bfa90d89c050a3ef8@ec2-54-221-234-62.compute-1.amazonaws.com:5432/dn7coi02b1hab"])

#Python3
###urllib.parse.uses_netloc.append("postgres")
###url = urllib.parse.urlparse(os.environ["postgres://vxjbtravsqldpn:8e28f8853a5ad91bb6ec8614359773e844b6afbe8e57324bfa90d89c050a3ef8@ec2-54-221-234-62.compute-1.amazonaws.com:5432/dn7coi02b1hab"])                                  
    
###conn = psycopg2.connect(
###database=url.path[1:],
###user=url.username,
###password=url.password,
###host=url.hostname,
###port=url.port
###)                                   

##################################

try:
    urlparse.uses_netloc.append("postgres") 
    connection_params = urlparse.urlparse(os.environ["DATABASE_URL"])
    db_connection = psycopg2.connect(database = connection_params.path[1:], user = connection_params.username, password = connection_params.password, host = connection_params.hostname, port = connection_params.port)
except:
    print "Database connection failed."

    
    
# Flask app should start in global layout
app = Flask(__name__)


@app.route('/webhook', methods=['POST'])
def webhook():
    req = request.get_json(silent=True, force=True)

    print("Request:")
    print(json.dumps(req, indent=4))

    res = makeWebhookResult(req)

    res = json.dumps(res, indent=4)
    print(res)
    r = make_response(res)
    r.headers['Content-Type'] = 'application/json'
    return r

def makeWebhookResult(req):

    result = req.get("result")
    parameters = result.get("parameters")
    city = parameters.get("city")

    resolvedQuery = parameters.get("resolvedQuery")
    attraction = parameters.get("attraction")    

    
    

    ###speech = "There are nice" + attraction #+ "places in " + city + "to have" + resolvedQuery + " and I will tell you about them. " #+ str(cost[zone])
    ##working### speech = "There are nice places in " + city + " and I will tell you about them. "
    #speech = "There are nice " + attraction + " to have " + resolvedQuery + "places in " + city + " and I will tell you about them. "
    #speech = "There are nice places in " + city + attraction + resolvedQuery + " and I will tell you about them. "
    speech = "Hmm, I'll tell you about the best places in " + city + " to have " + attraction
    
    print("Response:")
    print(speech)
    return {
        "speech": speech,
        "displayText": speech,
        #"data": {},
        #"contextOut": [],
        ##"source": "travelsourse"
    }

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))

    print ("Starting app on port %d" %(port))

    app.run(debug=True, port=port, host='0.0.0.0')
