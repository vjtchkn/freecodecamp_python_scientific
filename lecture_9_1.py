names = ["csev", "cwen", "csev", "zqian", "cwen"]

# Count the number of names using a dictionary
counts = dict()
for name in names:
    if name not in counts:
        counts[name] = 1
    else:
        counts[name] += 1
print(counts)

# Use the get method
counts = dict()
for name in names:
    counts[name] = counts.get(name, 0) + 1
print(counts)
