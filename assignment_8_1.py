# Build a list of unique words in a file
# Open file romeo.txt, read it line by line
# For each line split it into a list of words
# For each word check if it is already in the list, otherwise add it
# Sort and print the unique words

fhand = open("romeo.txt")
vocabulary = list()

for line in fhand:
    words = line.split()
    for word in words:
        if word in vocabulary:
            continue
        else:
            vocabulary.append(word)

vocabulary.sort()
print(vocabulary)
