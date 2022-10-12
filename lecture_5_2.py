# Propmpt user for input until they input 'done', otherwise print it
# If the input starts with '#' then do not print it

while True:
    line = input("> ")
    if line[0] == "#":
        continue
    if line == "done":
        break
    print(line)
print("Done!")
