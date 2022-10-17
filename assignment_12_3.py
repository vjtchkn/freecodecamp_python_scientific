# Replicate socket program using urllib
# Disregard header
import urllib.request

url = input("Enter URL: ")
if len(url) == 0:
    url = "http://data.pr4e.org/romeo.txt"

fhand = urllib.request.urlopen(url)

document = ""
for line in fhand:
    document += line.decode()

print(document[:3000])
print(f"Total characters: {len(document)}")
