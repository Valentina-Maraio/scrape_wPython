This project needs this version of urllib3
pip install urllib3==1.25.10


# **Code Explanation:**

This code is a Python script that scrapes a Wikipedia page to extract information about English novelists.
It uses libraries like pandas, requests, BeautifulSoup, time, and re for web scraping, data manipulation, and handling regular expressions.
The script sends an HTTP GET request to the Wikipedia page, parses the HTML content using BeautifulSoup, and then extracts relevant information about authors from the page.
It extracts author names, birth dates, and death dates (if available) from the HTML code.
The extracted data is then stored in a list of dictionaries where each dictionary represents an author's information.
The script then sorts the author names alphabetically, creates a pandas DataFrame from the extracted data, adds a delay to avoid overwhelming the website with requests, and finally exports the data to a JSON file named authors_names_1900s.json.

# **Documentation:**
### Purpose:
This script scrapes Wikipedia for a list of English novelists and their birth/death dates.

## Libraries Used:
pandas: For data manipulation and creating a DataFrame.
