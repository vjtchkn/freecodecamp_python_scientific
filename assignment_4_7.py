# Prompt the user for a score between 0 and 1
# If the score is out of range print an error and exit
# Print grade based on score
# Define function computegrade

score = input("Enter Score: ")

try:
    score = float(score)
except:
    print("Provided score is not a number")
    exit()


def computegrade(s):
    if score < 0 or score > 1:
        return "Provided score out of range"
    elif score < 0.6:
        return "F"
    elif score < 0.7:
        return "D"
    elif score < 0.8:
        return "C"
    elif score < 0.9:
        return "B"
    else:
        return "A"


print(computegrade(score))
