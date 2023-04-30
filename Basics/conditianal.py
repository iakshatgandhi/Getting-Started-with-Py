a = int(input("Enter your age "))
if(a>=18):
    print("You can Drive")
else:
    print("You can't")



print(id(a))
'''
One interesting thing to note while working with Python variables is that when
we create a variable, we actually create an object somewhere in the memory 
with a unique mapping or ID/Address. We can see this unique ID generated 
against each object using id().
'''