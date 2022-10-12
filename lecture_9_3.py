# Iterate over a dictionary
counts = {"chuck": 1, "fred": 42, "jan": 100}
for key in counts:
    print(key, counts[key])

# 2 variable iteration over tuples
for key, value in counts.items():
    print(key, value)
