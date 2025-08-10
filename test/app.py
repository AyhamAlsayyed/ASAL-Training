def odd_even (num):
    if(bool(num%2)):
        return "odd"
    else:
        return "even"
        
print(f"the number 5 is {odd_even(5)}, and the number 8 is {odd_even(8)}")

class person:
    def __init__(self, name, age, num):
        self.name = name
        self.age = age
        self.num = num

    def info(self):
        return (f"the perosn named {self.name} have a {self.num} number, and he is {self.age} years old.")
    
p1 = person("ahmad", 20, 1)
print(p1.info())

fruit ={"apple" : 20 , "banana" : 4 , "grap" : 6}
for key in fruit:
    print(key, fruit[key])

vege = ["onion", "potato", "papper"]

for i in vege:
    print (i)

print("hello")