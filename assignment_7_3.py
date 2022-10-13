# Modify previous program by adding an easter egg

fname = input("Enter file name: ")

if fname == "na na boo boo":
    print("NA NA BOO BOO - You have been punk'd")
    exit()

fh = open(fname)

count = 0
confidence_total = 0

for line in fh:
    if not line.startswith("X-DSPAM-Confidence:"):
        continue
    else:
        count += 1
        col_pos = line.find(":")
        confidence_total += float(line[col_pos + 1 :].strip())

confidence_average = confidence_total / count

print("Average spam confidence:", confidence_average)
