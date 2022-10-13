# Categorize each mail by day of the week
# Look for lines starting with "From" and the third word
# Print out counts for each day

fname = input("Enter a file name: ")
fhand = open(fname)

days_dict = dict()
for line in fhand:
    if not line.startswith("From "):
        continue
    else:
        words = line.strip().split()
        day = words[2]
        days_dict[day] = days_dict.get(day, 0) + 1

print(days_dict)
