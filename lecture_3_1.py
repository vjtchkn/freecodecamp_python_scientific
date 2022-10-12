astr = "Hello Bob"

try:
    istr = int(astr)
except:
    istr = -1

print("First", istr)

bstr = "123"
try:
    jstr = int(bstr)
except:
    jstr = -1

print("Second", jstr)
