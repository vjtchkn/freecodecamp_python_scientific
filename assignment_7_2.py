# Extract the number at the end of the given string
# Using find() and slicing []
# Convert to floating point and print out

text = "X-DSPAM-Confidence:    0.8475"

colon_pos = text.find(":")
number = float(text[colon_pos + 1 :].strip())
print(number)
