# Extract email domain
import re

lin = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("@([^ ]*)", lin)
print(y)

# Use only lines srarting with "From "
y = re.findall("^From .*@([^ ]*)", lin)
print(y)

# Extract spam confidence and find the maximum
hand = open("mbox-short.txt")
numlist = list()
for line in hand:
    line = line.strip()
    conf = re.findall("^X-DSPAM-Confidence: ([0-9.]+)", line)
    if len(conf) != 1:
        continue
    num = float(conf[0])
    numlist.append(num)
print("Maximum:", max(numlist))
