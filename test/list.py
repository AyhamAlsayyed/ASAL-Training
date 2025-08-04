list = ["stone", "iron", "copper", "coal", "glass", "sand"]
list2 = ["grass", "soil"]

print(list[2])
list[2] = "tin"
print(list[2])

list.append("plastic")
list.insert(0, "water")
list.remove("coal")
list.pop(3)
print(list, len(list))

list += list2

print(list)