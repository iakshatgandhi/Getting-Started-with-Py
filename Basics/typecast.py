a = "1"
b = "4"

print(a+b)

print(int(a) + int(b))


c = 5
print(type(c))
d = 5.5
print(type(d))


print(c + d,"type is",type(c+d))

# python always type casts to the higher priority data type like here 
# if the output gets returned to int  type then the date lose happens so 
# pythons type casts the int into float and then returns float as output 