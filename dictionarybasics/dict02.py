my_dict = {
    "apple": 2.99,
    "banana": 1.25,
    "cherry": 4.50,
    "durian": 7.99,
    "elderberry": 2.00,
    "lemon": 1.00,
    "grape": 1.75,
    "honeydew": 3.25,
    "kiwi": 0.99,
    "fig": 3.50
}
# In this dictionary, each key represents a type of fruit
# and each value represents the price of that fruit. 
# You can access the value of a specific key using the square 
# bracket notation, like so:

print(my_dict["apple"])
print(my_dict.popitem())
# removes the last item
print(my_dict.pop("durian")) # printing the value of the popped one 


print(my_dict)

print("durian" in my_dict)
print("grape" in my_dict)
print(my_dict.keys())

# also we can pass this into list as well
print(list(my_dict.keys()))


print(my_dict.values())
print(list(my_dict.values()))


# all items in the dictionary into a list
print(list(my_dict.items()))