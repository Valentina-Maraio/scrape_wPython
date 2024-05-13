# scrape the wikipedia for Authors' names
import pandas as pd
import requests

from bs4 import BeautifulSoup
import time

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
        name = li.find('a').get_text()
        authors.append(name)

# Sort the authors' names alphabetically
# authors.sort()

# Store the information in a pandas dataframe
df = pd.DataFrame(authors, columns=['Name'])

# Add a delay between requests to avoid overwhelming the website with requests
time.sleep(1)

# Export the data to a CSV file
df.to_json('authors_names_1900s.json', index=False)
