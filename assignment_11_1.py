# Ask user to enter regular expression
# Count the number of lines that match
import re

fhand = open("mbox.txt")

expr = input("Enter a regular expression: ")

match = 0
for line in fhand:
    if re.search(expr, line):
        match += 1

print(f"mbox.txt had {match} lines that matched {expr}")
