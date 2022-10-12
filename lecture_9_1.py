# Create a list and change a specific value in it
lotto = [2, 14, 24, 41, 63]
print(lotto)
lotto[2] = 30
print(lotto)

# 2 ways to loop through a list
friends = ["Adam", "Betty", "Cindy"]

for friend in friends:
    print("Hello", friend)

for i in range(len(friends)):
    friend = friends[i]
    print("Goodbye", friend)

# List methods
stuff = list()
stuff.append("book")
stuff.append("apple")
stuff.append("computer")
print(stuff)

stuff.sort()
print(stuff)

# in operator
print("book" in stuff)

# Ask user for numbers and repeatedly return average using a list
numlist = list()
while True:
    inp = input("Enter a number: ")
    if inp == "done":
        break
    else:
        numlist.append(float(inp))
average = sum(numlist) / len(numlist)
print("Average:", average)

# Print days of the week from email log
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.strip()
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        print(words[2])

# Print email domains
fhand = open("mbox-short.txt")
for line in fhand:
    line = line.strip()
    if not line.startswith("From"):
        continue
    else:
        email = line.split()[1]
        domain = email.split("@")[1]
        print(domain)
