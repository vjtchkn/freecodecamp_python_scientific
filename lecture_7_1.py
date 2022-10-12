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

# Print lines starting with "From:"
short = open("mbox-short.txt", "r")
for line in short:
    line = line.strip()
    if line.startswith("From:"):
        print(line)

# Print all lines from @uct.ac.za
short = open("mbox-short.txt", "r")
for line in short:
    line = line.strip()
    if not "@uct.ac.za" in line:
        continue
    print(line)

# Make the file name a user input and count the lines starting with "Subject:"
# Catch error if the file does not exist
fname = input("Enter the file name: ")
try:
    fhand = open(fname, "r")
except:
    print("File cannot be opened:", fname)
    quit()

count = 0
for line in fhand:
    line = line.strip()
    if line.startswith("Subject:"):
        count += 1
print("There were", count, "subject lines in", fname)
