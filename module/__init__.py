from flask import Flask
from pymongo import MongoClient
import urllib.parse as up


# Mongo DB
Host = '161.82.174.10'
Port = '27017'
UserName = up.quote_plus('bluzen')
Password = up.quote_plus('8luzen18!@')
url = 'mongodb://%s:%s@%s:%s' % (UserName, Password, Host, Port)
mongo = MongoClient(url)

app = Flask(__name__.split('.')[0], template_folder="../htdocs/templates/", static_folder="../htdocs/resources/")