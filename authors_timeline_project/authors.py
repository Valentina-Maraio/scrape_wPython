# scrape the wikipedia for Authors' names
import pandas as pd
import requests
from bs4 import BeautifulSoup
import time
import re

# URL of the website to scrape
url = "https://en.wikipedia.org/wiki/List_of_English_novelists"

# Send an HTTP GET request to the website
res = requests.get(url)

# Parse the HTML code using BeautifulSoup
soup = BeautifulSoup(res.content, 'html.parser')

# Extract the relevant information from the HTML code
authors = []
for ul in soup.select('div.div-col ul'):
    for li in ul.find_all('li'):
        # Extract the data in the double quotes
        text = li.get_text(strip=True)
        date = re.search(r'\((.*?)\)', text).group(1) if re.search(r'\((.*?)\)', text) else None
        name = li.find('a').get_text()

        if date and '\u2013' in date:
            birth, *death = date.split('\u2013', 1)
            death = '\u2013'.join(death)
        else:
            birth = date.strip() if date else None
            death = None

        authors.append({'author_name': name, 'birth': birth, 'death': death})

# Sort the authors' names alphabetically
# authors.sort()

# Store the information in a pandas dataframe
df = pd.DataFrame(authors)

# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)

# Export the data to a CSV file
df.to_json('authors_names_1900s.json', orient='records', index=False)
