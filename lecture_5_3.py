# Find the largest number from a list of numbers
largest_n = None
numbers = [9, 41, 12, 3, 74, 15]

for n in numbers:
    if largest_n is None:
        largest_n = n
        continue
    if n > largest_n:
        largest_n = n

print("The largest number is", largest_n)


# Find numbers higher than 20 from a list of numbers
for n in numbers:
    if n > 20:
        print("Large number:", n)

# Find if number 3 in a list of numbers
found = False

for n in numbers:
    if n == 3:
        found = True
        break

print(found)

# Find the smallest number from a list of numbers
smallest_n = None

for n in numbers:
    if smallest_n is None:
        smallest_n = n
        continue
    if n < smallest_n:
        smallest_n = n

print("The smallest number is", smallest_n)
