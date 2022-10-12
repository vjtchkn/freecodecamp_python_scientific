rawstr = input("Enter a positive number: ")

try:
    ival = int(rawstr)
except:
    ival = -1

if ival > 0:
    print("Nice work")
else:
    print("Not a positive number")
