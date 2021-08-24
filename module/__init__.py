from flask import Flask
from pymongo import MongoClient


mongo = MongoClient("161.82.174.10", 27017)
app = Flask(__name__.split('.')[0], template_folder="../htdocs/templates/", static_folder="../htdocs/resources/")