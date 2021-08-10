from flask import Flask

app = Flask(__name__.split('.')[0], template_folder="../htdocs/templates/", static_folder="../htdocs/resources/")