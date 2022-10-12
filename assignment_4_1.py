# Prompt user for hours and hourly rate
# Calculate gross pay using function
# Hours above 40 have 1.5 times hourly rate


def computepay(h, r):
    if h <= 40:
        return h * r
    else:
        return 40 * r + (h - 40) * r * 1.5


hours = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))

pay = computepay(h=hours, r=rate)
print("Pay", pay)
