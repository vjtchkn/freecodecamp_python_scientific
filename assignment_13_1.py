import urllib.request
import xml.etree.ElementTree as ET

# Prompt for URL
url = input("Enter location: ")

# Read XML data from URL using urllib
print("Retrieveing", url)
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "characters")

# Parse and extract comment counts
tree = ET.fromstring(data)
comments = tree.find("comments")

counts = []
for comment in comments:
    counts.append(int(comment.find("count").text))

# Compute the sum of numbers
print("Count:", len(counts))
print("Sum:", sum(counts))
