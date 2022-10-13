# Define a function that counts the number of specified letters in a word


def count(w, l):
    count = 0
    for letter in w:
        if letter == l:
            count = count + 1
    return count


print(count("banana", "a"))
print(count("apple", "a"))
