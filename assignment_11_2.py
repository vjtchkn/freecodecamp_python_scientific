# Look for lines in the form New Revision: number
# Extract the numbers, compute average and print as integer
from audioop import avg
import re

fname = input("Enter file: ")
fhand = open(fname)

numbers = list()
for line in fhand:
    found = re.findall("New Revision: ([0-9]+)", line)
    if len(found) == 0:
        continue
    else:
        for item in found:
            numbers.append(int(item))

print(int(sum(numbers) / len(numbers)))
