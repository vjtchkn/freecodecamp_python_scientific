# Read through a file, print the contents line by line all in upper case
file = input("Enter a file name: ")
handle = open(file)

for line in handle:
    print(line.upper())
