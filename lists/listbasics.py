test_list = ["R", 1, "Test", True]

print("R" in test_list)
print("U" in test_list)
print(test_list[0])

test_list[2] = "^_^" 
print(test_list[2])
print("^_^" in test_list[-2])

# slicing
print(test_list[2:])

# append
test_list.append("apple")
print(len(test_list))

# extend list
test_list.extend(["roger", 56, "charlie"])
print(test_list)
test_list += [33, 67]
print(test_list)

# remove
test_list.remove("R")
print(test_list)

# pop
print(test_list.pop())
print(test_list)

# inserting item in the middle of the list
test_list.insert(3,"Akshat")
print(test_list)
                # for inserting we use slicing
test_list[3:3] = ["My","self"]
print(test_list)

# sorting in the list it won't work work in the str and int list only in the list with str items 
list1 = ["kar", "Ror", "Sam", "Eup", "Que", "Abc", "abc"]
items = list1[:] # copying of the list items
list1.sort()  # it sorts the upper letter firsts and then the lower letter u can fix this via 
print(list1)
# via this .......
list1.sort(key=str.lower)
print(list1)
# copy of the original
print(items)


# !!! Important note 
# to sort items there is also a global function sorted where we need to pass in two arguments that is 
# list name and the key i.e like here key = str.lower
# sorted function does not alter the original list instead it sorts the list in a new list............