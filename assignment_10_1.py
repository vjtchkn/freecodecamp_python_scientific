# Read throught file, extract email addresses from lines startin with "From "
# Count the number of messages from each person using a dictionary
# Print the person with the most commits using sorting on a list of tuples

fname = input("Enter a file name: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    if not line.startswith("From "):
        continue
    email = line.split()[1]
    counts[email] = counts.get(email, 0) + 1

top_address = sorted(
    [(count, email) for (email, count) in counts.items()], reverse=True
)[0]
print(top_address[1], top_address[0])
