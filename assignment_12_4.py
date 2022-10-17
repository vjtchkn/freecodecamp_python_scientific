# Change the url links program
# Extract and cound (p) paragraph tags
# Display the number of paragraphs (without the text)

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup

url = input("Enter URL: ")
if len(url) == 0:
    url = "http://www.dr-chuck.com/page1.htm"

html = urllib.request.urlopen(url).read()

soup = BeautifulSoup(html, "html.parser")

tags = soup("p")
count = 0
for tag in tags:
    count += 1

print("Number of paragraphs:", count)
