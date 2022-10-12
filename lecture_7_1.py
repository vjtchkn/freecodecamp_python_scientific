# Iterate through a string and print out individual characters
fruit = "banana"
for letter in fruit:
    print(letter)


# Count the number of letter 'a'
count = 0
for letter in fruit:
    if letter == "a":
        count += 1
print(count)


# Check if 'a' is in the word
if "a" in fruit:
    print("Found it!")


# Find and extract school host from email header
header = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
at_pos = header.find("@")
print(at_pos)
space_pos = header.find(" ", at_pos)
print(space_pos)
domain = header[at_pos + 1 : space_pos]
print(domain)
