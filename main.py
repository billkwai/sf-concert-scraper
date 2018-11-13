#!/usr/bin/env python
from flask import Flask
from bs4 import BeautifulSoup
from scrape import scrape

app = Flask(__name__)

@app.route('/')
	return 0

if __name__=='__main__':
	app.run(debug=True)
