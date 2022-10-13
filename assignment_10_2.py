# Read through a file
# Find distribution by hour aof the day
# Using lines starting with "From "
# Print counts sorted by hours

name = input("Enter file: ")
if len(name) < 1:
    name = "mbox-short.txt"
handle = open(name)

hours = dict()
for line in handle:
    if not line.startswith("From "):
        continue
    else:
        words = line.split()
        time = words[5]
        hour = time.split(":")[0]
        hours[hour] = hours.get(hour, 0) + 1

for hour, count in sorted(hours.items()):
    print(hour, count)
