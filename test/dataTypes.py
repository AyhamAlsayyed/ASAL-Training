x = "hello"
print(f"the {x} is a {type(x)}")
x = 10
print(f"the {x} is a {type(x)}")
x = 10.2
print(f"the {x} is a {type(x)}")
x = 10j
print(f"the {x} is a {type(x)}")
x = [1, 2, 3, 4, 5, 6]
print(f"the {x} is a {type(x)}")
x = {1, 2, 3, 4, 5, 1}#the dublicat well be removed
print(f"the {x} is a {type(x)}")
x = {"one" : 1, "two" : 2, "three" : 3}
print(f"the {x} is a {type(x)}")
x = frozenset({"10", "20", "30"})
print(f"the {x} is a {type(x)}")
x = b"Hello"	
print(f"the {x} is a {type(x)}")
x = bytearray(5)
print(f"the {x} is a {type(x)}")