tupleone = ("zero", "one", "two", "three", "five")
tupletwo = ("five",)
print(tupleone[3])

#if you want to add item into the tuple you have to change it into a list 
tupleone = list(tupleone)
tupleone.append("four")
tupleone.remove("five")
tupleone = tuple(tupleone)
print(tupleone[4])
print(type(tupleone))

#or merge it with another tuple

tupletwo = tupleone + tupletwo

print(f"the 2nd tuple is {tupletwo}")

zero, one, two, *nums = tupleone

print(zero)
print(one)
print(two)
print(nums)

print('the nums in the tuple are: ')
for num in tupleone:
    print(num)