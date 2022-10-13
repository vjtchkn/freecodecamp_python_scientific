# A while loop that prints letters in a word backwards

word = input("Word: ")

index = len(word) - 1

while index >= 0:
    print(word[index])
    index -= 1
