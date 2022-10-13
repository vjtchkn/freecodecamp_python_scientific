# Read words in words.txt, store them in a dictionary
# Use in operator to check whether a string is in a dictionary

file = "words.txt"
handle = open(file)

words = dict()

for line in handle:
    ws = line.split()
    for w in ws:
        words[w] = words.get(w, 0) + 1

search = input("Search for a word: ")
print(search in words)
