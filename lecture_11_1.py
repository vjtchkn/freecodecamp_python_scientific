# Regular expressions
import re

# # Contains
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("From:", line):
        print(line)

# Starts with
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^From:", line):
        print(line)

# Starts with X and matches pattern of any characters before :
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^X.*:", line):
        print(line)

# Starts with X- followed by at least one non white space character before :
hand = open("mbox-short.txt")
for line in hand:
    line = line.rstrip()
    if re.search("^X-\S+:", line):
        print(line)
