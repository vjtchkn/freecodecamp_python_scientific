# Read in mbox.txt, print the object
long = open("mbox.txt", "r")
short = open("mbox-short.txt", "r")
print(long)
print(short)

# Print lines in the file using a for loop
# for line in short:
#     print(line)

# Count the number of lines in the file
long = open("mbox.txt", "r")
count = 0
for line in long:
    count += 1
print("Line count:", count)

# Read file as a string
short = open("mbox-short.txt", "r")
text = short.read()
print(len(text))
print(text[:20])

# Print lines starting with From:
short = open("mbox-short.txt", "r")
for line in short:
    line = line.strip()
    if line.startswith("From:"):
        print(line)
