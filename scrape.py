from bs4 import BeautifulSoup
import requests

def scrape():
  return scrape_fillmore()

def scrape_fillmore():
  url = "http://thefillmore.com/calendar/?m=December"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.text, 'html.parser')

  events_this_month = soup.find_all('p', class_='title')
  return [events.contents for events in events_this_month]

