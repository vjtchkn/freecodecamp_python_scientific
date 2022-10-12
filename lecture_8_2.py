# Debugging tutorial
# Parse mbox-short.txt and extract the days of the week

han = open("mbox-short.txt")

for line in han:
    line = line.rstrip()
    wds = line.split()
    print("Line:", line)
    print("Words:", wds)

    # Guardian pattern
    if len(wds) < 3:
        print("Ignore")
        continue

    if wds[0] != "From":
        print("Ignore")
        continue
    print(wds[2])
