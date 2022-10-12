# Read through provided txt file
# Find who has sent the most email messages
# Use lines with 'From ' and the second word from those lines as the person
# Create a dictionary mapping sender to a count and read through it using a max loop
# Print the email and the count at the end

name = input("Enter file:")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

counts = dict()

for line in handle:
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        sender = words[1]
        counts[sender] = counts.get(sender, 0) + 1

max_sender = None
max_count = None

for sender, count in counts.items():
    if max_sender == None or count > max_count:
        max_sender = sender
        max_count = count

print(max_sender, max_count)
