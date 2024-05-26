import pandas as pd
import requests
from bs4 import BeautifulSoup
import time

first_page = 'https://archiveofourown.org/works/search?work_search%5Bquery%5D=Good+omens&work_search%5Btitle%5D=&work_search%5Bcreators%5D=&work_search%5Brevised_at%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcrossover%5D=F&work_search%5Bsingle_chapter%5D=0&work_search%5Bword_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bfandom_names%5D=&work_search%5Brating_ids%5D=&work_search%5Bcharacter_names%5D=&work_search%5Brelationship_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Bcomments_count%5D=&work_search%5Bbookmarks_count%5D=&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&commit=Search'
second_page = 'https://archiveofourown.org/works/search?commit=Search&page=2&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=F&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bquery%5D=Good+omens&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D='
third_page = 'https://archiveofourown.org/works/search?commit=Search&page=3&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=F&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bquery%5D=Good+omens&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D='
forth_page = 'https://archiveofourown.org/works/search?commit=Search&page=3&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=F&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bquery%5D=Good+omens&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D='
fifth_page = 'https://archiveofourown.org/works/search?commit=Search&page=5&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=F&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bquery%5D=Good+omens&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D='
sixth_page = 'https://archiveofourown.org/works/search?commit=Search&page=6&work_search%5Bbookmarks_count%5D=&work_search%5Bcharacter_names%5D=&work_search%5Bcomments_count%5D=&work_search%5Bcomplete%5D=T&work_search%5Bcreators%5D=&work_search%5Bcrossover%5D=F&work_search%5Bfandom_names%5D=&work_search%5Bfreeform_names%5D=&work_search%5Bhits%5D=&work_search%5Bkudos_count%5D=&work_search%5Blanguage_id%5D=en&work_search%5Bquery%5D=Good+omens&work_search%5Brating_ids%5D=&work_search%5Brelationship_names%5D=&work_search%5Brevised_at%5D=&work_search%5Bsingle_chapter%5D=0&work_search%5Bsort_column%5D=kudos_count&work_search%5Bsort_direction%5D=desc&work_search%5Btitle%5D=&work_search%5Bword_count%5D='

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
