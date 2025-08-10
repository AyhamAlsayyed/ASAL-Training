x = "I have a lot of apple's in my house!, Do you have the same?."
#0000012345678901234567890123456789012345678901234567890123456789
y = x.strip()
print(f"the 7th latter of the text is {y[6]}")
#I used y here to count only the latter by removing the whitespace
count = 0

for i in x:
    if i.islower() or not " ":
        count+=1

print(f"the txt have {count} lower case latter's")

print(f"the word house is in the txt: {'house' in x }")
print(f"the hi me is in the txt: {'hi' in x }")

print(x[:36])
print(x[38:])
print(x[16:23])

print(x.split(","))