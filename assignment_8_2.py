# Open mbox-short.txt, read line by line
# For lines that start with "From " print the email adress
# At the end print out count of such lines

fname = input("Enter file name: ")
if len(fname) < 1:
    fname = "mbox-short.txt"

fh = open(fname)
count = 0

for line in fh:
    if not line.startswith("From "):
        continue
    else:
        print(line.split()[1])
        count += 1

print("There were", count, "lines in the file with From as the first word")
