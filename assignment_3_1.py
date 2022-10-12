# Ask the user for number of hours and hourly rate
# Calculate gross pay with any hours above 40 have the rate of 1.5 times the basic rate
# Display the gross pay to the user

hours = input("Enter Hours: ")
hours = float(hours)

rate = input("Enter Rate: ")
rate = float(rate)

if hours <= 40:
    pay = hours * rate
else:
    pay = 40 * rate + (hours - 40) * rate * 1.5

print(pay)
