import pandas as pd
import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from urllib.parse import urlparse, urlunparse
import time

main_play_list = 'https://www.opensourceshakespeare.org/views/plays/plays.php'

main_res = requests.get(main_play_list)

soup = BeautifulSoup(main_res.content, 'html.parser')

# in play = [] I have all the titles of the Shakespeare's Plays
plays = []
selected_play_links= []
for ul in soup.select('div ul'):
    for li in ul.find_all('li'):
        title = li.find('a').get_text()
        play_link = li.find('a')['href']
        parsed_link = main_play_list.replace("/plays.php", "/")
        final_link = parsed_link + play_link
        plays.append({'Plays': {'play_title': title, 'Play_Link': final_link}})
        selected_play_links.append({'links': final_link})

# in the selected_play_links = [] I have the link of each one of the plays.
# Now to get the Complete Play I need to access the link I currently have in selected_play_link array
# To do that I need to write a loop on the array and for each link make a call and write a for
# to get the 'Complete Play' link

df = pd.DataFrame(plays)
df_links = pd.DataFrame(selected_play_links)

time.sleep(1)

df.to_json('shakespeare_plays.json', index=False)
df_links.to_json('shakespeare_plays_links.json', index=False)

