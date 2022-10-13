# Ask the user for number of hours and hourly rate
# If non numberic imput entered, print error message and exit
# Calculate gross pay with any hours above 40 have the rate of 1.5 times the basic rate
# Display the gross pay to the user

hours = input("Enter Hours: ")
try:
    hours = float(hours)
except:
    print("Error, please enter numeric input")
    exit()

rate = input("Enter Rate: ")
try:
    rate = float(rate)
except:
    print("Error, please enter numeric input")
    exit()


if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * rate * 1.5

print(pay)
