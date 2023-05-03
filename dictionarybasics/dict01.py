stu_marks = {"aman":27, "rohan":60}
print(stu_marks["aman"])
stu_marks["aman"]=5

print(stu_marks)

print(stu_marks.get("acceptance","No"))
# here in the get function we defined the default value of the key as
# No if the value to the key is present in the dictionary then its going to pick
# that else it with pice the default value

print(stu_marks.pop("aman"))  # returns the popped item
print(stu_marks)  # item is popped


