import urllib.request
import json

# Prompt for location
location = input("Enter location: ")

# Retrieve JSON
api_key = 42
serviceurl = "http://py4e-data.dr-chuck.net/json?"

parms = dict()
parms["address"] = location
parms["key"] = api_key
url = serviceurl + urllib.parse.urlencode(parms)

print("Retrieving", url)
uh = urllib.request.urlopen(url)
data = uh.read().decode()
print("Retrieved", len(data), "characters")

# Parse data
js = json.loads(data)

# Retrieve the first place_id from the JSON
place_id = js["results"][0]["place_id"]
print("Place id", place_id)
