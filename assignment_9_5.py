# Read through provided txt file
# Find email domains and count them

fname = input("Enter a file name: ")
fhand = open(fname)

domains = dict()
for line in fhand:
    if not line.startswith("From "):
        continue
    else:
        email = line.strip().split()[1]
        domain = email.split("@")[1]
        domains[domain] = domains.get(domain, 0) + 1

print(domains)
