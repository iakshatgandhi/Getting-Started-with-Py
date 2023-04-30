a = input("enter the name ")
print("hello", a)
print("hello "+ a)

print("He said, I am sick, \"Actually\"")  #using escape sequence 
print('He said, I am sick, "Actually"')  #using different parentheses

str = '''
hey, Akshat
this is Rishab
need some time of yours 
'''                             # this is how multi line string is defined in python its use case is shown 
print(str)

str1 = '''
Python is currently the most widely used multi-purpose, high-level programming language.
Python allows programming in Object-Oriented and Procedural paradigms.
Python programs generally are smaller than other programming languages like Java. Programmers have to type relatively less and indentation requirement of the language, makes them readable all the time.
Python language is being used by almost all tech-giant companies like – Google, Amazon, Facebook, Instagram, Dropbox, Uber… etc.
The biggest strength of Python is huge collection of standard library which can be used for the following:
	Machine Learning
	GUI Applications (like Kivy, Tkinter, PyQt etc. )
	Web frameworks like Django (used by YouTube, Instagram, Dropbox)
	Image processing (like OpenCV, Pillow)
	Web scraping (like Scrapy, BeautifulSoup, Selenium)
	Test frameworks
	Multimedia
	Scientific computing
	Text processing and many more..

'''
print (str1)

print("--------------------------------------------------------------------------------------------------")
# accessing the string element with the indexing
print(a[0])
print(a[1])
print("--------------------------------------------------------------------------------------------------")
for char in a:
    print(char)
