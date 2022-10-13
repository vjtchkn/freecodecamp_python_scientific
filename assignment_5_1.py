# Prompt user for numbers until 'done' is entered
# Print out total, count and average of the numbers
# Detect if user enters something besides a number

total = 0
count = 0

while True:
    number = input("Enter a number: ")
    if number == "done":
        break

    try:
        number = float(number)
    except:
        print("Invalid input")
        continue
    total += number
    count += 1

print("Total:", total, "Count:", count, "Average:", total / count)
