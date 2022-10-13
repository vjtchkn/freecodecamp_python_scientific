# Repeatedly prompt the user for integers until 'done' is entered
# Print out the largest and smallest of the numbers
# If non-integer is entered, ignore it and reprompt the user

largest = None
smallest = None
numbers = []

while True:
    num = input("Enter a number: ")
    if num == "done":
        break
    else:
        try:
            num = int(num)
        except:
            print("Invalid input")
            continue
        else:
            numbers.append(num)

for n in numbers:
    if largest is None or smallest is None:
        largest = n
        smallest = n
    else:
        if n > largest:
            largest = n
        if n < smallest:
            smallest = n

print("Maximum is", largest)
print("Minimum is", smallest)
