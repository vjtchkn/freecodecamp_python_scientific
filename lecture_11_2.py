# Matching and extracting data
import re

# Extract strings with one or more digits
x = "My 2 favorite numbers are 19 and 42."
y = re.findall("[0-9]+", x)
print(y)

# Extract email adress
x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("\S+@\S+", x)
print(y)

# Limit extracting string
x = "From stephen.marquard@uct.ac.za Sat Jan 5 09:14:16 2008"
y = re.findall("From (\S+@\S+)", x)
print(y)
