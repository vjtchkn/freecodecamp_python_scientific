# Repeatedly ask user for numbers until user enters 'done'
# Store numbers in a list
# Use max() and min() functions and print them for the user

numbers = list()

while True:
    number = input("Enter a number: ")
    if number == "done":
        break
    try:
        number = float(number)
    except:
        print("Not a number")
        continue
    numbers.append(number)

print("Maximum:", max(numbers))
print("Minimum:", min(numbers))
