# Read through a file with text and numbers
# Extract all the numbers and compute their sum

import re

fname = input("Enter text file: ")
fhand = open(fname)

numbers = list()
for line in fhand:
    ns = re.findall("[0-9]+", line)
    if len(ns) == 0:
        continue
    for n in ns:
        numbers.append(int(n))

print(f"Sum of numbers is {sum(numbers)}")
