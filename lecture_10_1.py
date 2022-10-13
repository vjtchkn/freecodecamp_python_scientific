# Sorting dictionary by keys
d = {"b": 1, "c": 20, "a": 10}
print(d.items())
print(sorted(d.items()))

# Sorting dictionary by values using tuples
c = {"b": 1, "c": 20, "a": 10}
print(c)

tmp = list()
for k, v in c.items():
    tmp.append((v, k))
print(tmp)

tmp = sorted(tmp, reverse=True)
print(tmp)

# Sorting using list comprehension
c = {"b": 1, "c": 20, "a": 10}
print(c)
print(sorted([(v, k) for k, v in c.items()]))
