import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

first_page = ''
second_page = ''
third_page = ''
forth_page = ''
fifth_page = ''
sixth_page = ''

req = requests.get(sixth_page)

soup = BeautifulSoup(req.content, 'html.parser')

page_one_titles = []
for ol in soup.find_all('ol'):
    for li in ol.find_all('h4'):
        title = li.find('a').get_text()
        page_one_titles.append({'Title': title})

df = pd.DataFrame(page_one_titles)

time.sleep(1)

df.to_json('title_page_6.json', index=True)
