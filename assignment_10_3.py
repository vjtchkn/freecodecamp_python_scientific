# Read a file
# Print letters in decreasing order of frequency
# Convert all input to lowercase ignore all spaces, digits, punctuation

fname = input("Enter file name: ")
fhand = open(fname)

counts = dict()
for line in fhand:
    line = line.lower()
    words = line.split()
    for word in words:
        for letter in word:
            if not letter.isalpha():
                continue
            else:
                counts[letter] = counts.get(letter, 0) + 1

counts_sorted = sorted(
    [(count, letter) for letter, count in counts.items()], reverse=True
)
for pair in counts_sorted:
    print(pair[1], pair[0])
