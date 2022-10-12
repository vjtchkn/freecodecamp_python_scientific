# Prompt user for file name, open the file
# Read throught the file and count lines containing 'X-DSPAM-Confidence:'
# Extract floating point values from each line and compute average of those values
# Print the average for the user
# Use the file name mbox-short.txt as the file name

fname = input("Enter file name: ")
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
