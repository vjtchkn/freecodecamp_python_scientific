# Web scraping with Beautiful Soup
import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

# Read the whole html file
url = "http://www.dr-chuck.com/page1.htm"
html = urllib.request.urlopen(url).read()

# Create a soup object
soup = BeautifulSoup(html, "html.parser")

# Retrieve all anchor tags - find links
tags = soup("a")
for tag in tags:
    print(tag.get("href", None))
