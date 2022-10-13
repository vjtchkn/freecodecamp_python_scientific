# Function called chop() that takes a list and modifies it
# Removing the first and last element and returns None

# Function called middle() that takes a list and returns a new list
# Containing all but the first and last elements

fruit = ["apple", "banana", "orange", "pear"]


def chop(lst):
    del lst[0]
    del lst[-1]
    return None


print(fruit)
chop(fruit)
print(fruit)


fruit = ["apple", "banana", "orange", "pear"]


def middle(lst):
    return lst[1:-1]


print(middle(fruit))
