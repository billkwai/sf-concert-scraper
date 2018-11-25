#!/usr/bin/env python
from flask import Flask
from bs4 import BeautifulSoup
from flask_sqlalchemy import SQLAlchemy
from scrape import scrape
import sys
import json
import os
from flask_heroku import Heroku

app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
heroku = Heroku(app)
db = SQLAlchemy(app)

@app.route('/data')
def get_data():
  return str(scrape())

if __name__=='__main__':
  port = int(os.environ.get('PORT', 5000))
  app.run(host='0.0.0.0', port=port)  #Start listening
