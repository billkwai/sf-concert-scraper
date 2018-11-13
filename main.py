#!/usr/bin/env python
from flask import Flask
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from scrape import scrape
import sys
import json
from flask_heroku import Heroku
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

app = Flask(__name__)

@app.route('/')
	return 0

if __name__=='__main__':
	app.run(debug=True)
