from bs4 import BeautifulSoup
import re
import requests
from datetime import datetime

def scrape():
  return scrape_fillmore()

def scrape_fillmore():
  event_list = []

  # regex
  event_date_re = '\w{3,9}?\s\d{1,2}?,\s\d{4}?'
  event_time_re = 'Show (\d:\d\d\sp.m.)'
  event_price_re = 'Tickets are (\$\d\d.\d\d)'
  
  url = "http://thefillmore.com/calendar"
  headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}
  page = requests.get(url, headers=headers)
  soup = BeautifulSoup(page.text, 'html.parser')

  all_events = soup.find_all('div', class_='faq_main calendar')
  for event in all_events:
    event_title_p = event.find('p', class_='title')
    event_title = event_title_p.a.string
    event_url = event_title_p.a.get('href')
    event_details = event.find('span', class_='content')
    event_details_string = str(event_details)


    event_date_raw = re.search(event_date_re, event_details_string).group(0)
    event_time_raw = re.search(event_time_re, event_details_string).group(1)
    event_price_raw = re.search(event_price_re, event_details_string).group(1)

    date_format = '%B %d, %Y'
    time_format = '%I:%M %p'
    datetime_format = to_datetime(event_date_raw, event_time_raw.replace('.', ''), date_format, time_format)

    event_list.append((event_title, event_url, datetime_format, event_price_raw))

  return event_list

def to_datetime(date, time, date_format, time_format):
  datetime_format = datetime.strptime(date + ' ' + time, date_format + ' ' + time_format)
  return datetime_format


