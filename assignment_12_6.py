# Scraping numbers from HTML using BeautifulSoup

from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# Connect to specified url and create the soup object
url = input("Enter URL: ")
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup("span")

comments_sum = 0
for tag in tags:
    comments_sum += int(tag.contents[0])

print(comments_sum)
