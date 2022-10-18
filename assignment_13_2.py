import urllib.request
import json

# Prompt for URL
url = input("Enter location: ")

# Read JSON data from URL using urllib
print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read()
print("Retrieved", len(data), "characters")

# Parse and extract comment counts
info = json.loads(data)
comments = info["comments"]
counts = []
for item in comments:
    counts.append(item["count"])

# Compute sum of counts
print("Count:", len(counts))
print("Sum:", sum(counts))
