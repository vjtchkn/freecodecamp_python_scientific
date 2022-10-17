# Follow link at specified positon a specified number of times
# Retrun the last name in sequence

import urllib.request
from bs4 import BeautifulSoup

# Prompt user for startin url and parameters
url = input("Enter URL: ")
count = int(input("Enter count: "))
position = int(input("Enter position: "))

# Follow through links in a loop
print(f"Retrieving: {url}")
for _ in range(count):
    # Create html handle
    html = urllib.request.urlopen(url).read()
    # Create a soup object
    soup = BeautifulSoup(html, "html.parser")
    # Retrieve anchor tags
    tags = soup("a")
    # Find the next URL
    url = tags[position - 1].get("href", None)
    print(f"Retrieving: {url}")
