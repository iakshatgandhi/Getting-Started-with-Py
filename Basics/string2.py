state = "UTTAR-PRADESH"
print(len(state))

name = "Akshat Gandhi"
print(name[0:6])

str = "Love"
print(str.upper())
print(str.lower())
'''
strings are immutable that is one can not change them inplace once created 
on applying any string method a new copy of string is created 
'''
str2 = "Hey!!!!!!"
print(str2.rstrip("!"))
# but it doesn't strips the starting characters

str3 = '''hey,
Akshat how are you'''

print(str3.replace("Akshat","Baby"))
# it replaces all occurrences in a string

str4 = "Please talk to me"
print(str4.split(" "))
# it returns output in list.

str5 = "introduction to python"
print(str5.capitalize())
# returns the fist letter capitalized and if by mistake any other character is in uppercase it even lowercase that as well

str6 = "Welcome to the Console!!!"
print(len(str6))
print(str6.center(80))
# add half half blank spaces to either sides 
print(len(str6.center(80)))


str7 = "hello hello love"
print(str7.count("hello"))
# prints the no of occurrences

str8 = "Welcome to the Console !!!"
print(str8.endswith("!!!"))
# returns bool output

str1 = "Welcome to the Console !!!"
print(str1.endswith("to", 7, 10)) 

# startswith() :
# The endswith() method checks if the string starts with a given value. If yes then return True, else return False.

str1 = "He's name is Dan. He is an honest man."
print(str1.find("is"))
print(str1.find("ish"))
# returns the first occurrence index 
# note computer can't detect that he's - he is it only reads the is first occurrence index here and if not present returns -1
# print(str1.index("ish"))
# in case we have to terminate the program with an error if the desired string is not found then we use index

str1 = "WelcomeToTheConsole"
print(str1.isalnum())
# The isalnum() method returns True only if the entire string only 
# consists of A-Z, a-z, 0-9. If any other characters or punctuations are present, then it returns False.

str1 = "Welcome"
print(str1.isalpha())
# The isalnum() method returns True only if the entire string only consists of A-Z, a-z. 
# If any other characters or punctuations or numbers(0-9) are present, then it returns False.

str1 = "hello world"
print(str1.islower())

str1 = "We wish you a Merry Christmas"
print(str1.isprintable())
# The isprintable() method returns True if all the values within the given string are printable, if not, then return False.

str5 = "hello \nWorld"
print(str5.isprintable())
# returns false cause \n is not printable character

str1 = "        "       #using Spacebar
print(str1.isspace())
str2 = "        "       #using Tab
print(str2.isspace())

# istitle() :
# The istitile() returns True only if the first letter of each word of the string is capitalized, else it returns False.

str2 = "To kill a Mocking bird"
print(str2.istitle())

# The isupper() method returns True if all the characters in the string are upper case, else it returns False.

str1 = "Python is a Interpreted Language" 
print(str1.swapcase())
# The swapcase() method changes the character casing of the string. Upper case are converted to lower case and lower case to upper case.

str1 = "He's name is Dan. Dan is an honest man."
print(str1.title())