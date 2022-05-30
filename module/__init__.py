from flask import Flask
from pymongo import MongoClient
import urllib.parse as up
import os

# Mongo DB
Host = os.environ['DB_HOST']
Port = os.environ['DB_PORT']
UserName = up.quote_plus(os.environ['DB_AUTH_ID'])
Password = up.quote_plus(os.environ['DB_AUTH_PW'])
url = 'mongodb://%s:%s@%s:%s' % (UserName, Password, Host, Port)
mongo = MongoClient(url)


# Mongo DB
Host_r = os.environ['DB_REPLICA_HOST']
Port_r = os.environ['DB_REPLICA_PORT']
UserName_r = up.quote_plus(os.environ['DB_REPLICA_AUTH_ID'])
Password_r = up.quote_plus(os.environ['DB_REPLICA_AUTH_PW'])
url_r = 'mongodb://%s:%s@%s:%s' % (UserName_r, Password_r, Host_r, Port_r)
mongo_r = MongoClient(url_r)



app = Flask(__name__.split('.')[0], template_folder="../htdocs/templates/", static_folder="../htdocs/resources/")