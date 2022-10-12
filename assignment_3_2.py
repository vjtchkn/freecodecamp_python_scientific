# Prompt the user for a score between 0 and 1
# If the score is out of range print an error and exit
# Print grade based on score

score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Provided score is not a number")

if score < 0 or score > 1:
    print("Provided score out of range")
elif score < 0.6:
    print("F")
elif score < 0.7:
    print("D")
elif score < 0.8:
    print("C")
elif score < 0.9:
    print("B")
else:
    print("A")
