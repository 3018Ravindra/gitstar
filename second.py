# learning python for beginners
# solving problems with python programming language

# my first problem in python is to print a message
print("i am here to solve problems")
print("this is for my cloud and devops journey")

# my second problem in python is to print a message with a variable
message = "i a solving problems with python"
print(message)

# my third problem in python is to print a message with a variable and a number
name = "ravi"
age = 25
print("my name is " + name + " and i am " + str(age) + " years old")

# my fourth problem in python is to print a message with a variable and a number using f-string
name = "ravi"
age = 25
print(f"my name is {name} and i am {age} years old")

# my fifth problem is to solve true or false
x = 5
y =10
print(x > y) #false
print(x < y) #true

# my sixth problem is to solve a math problem
a = 10
b = 15
print(a + b) #25
print(a - b) #-5
print(a * b) #150
print(a / b)
print(a % b) 
print(a ** b)
print(a // b)

# my seventh problem is to solve a problem with a function
def greet(name):
    return f"hello {name}, welcome to python programming"
print(greet("ravi"))

# my eighth problem is to solve a problem with a loop
for i in range(5):
    print(i)
for i in range(1, 6):
    print(i)

# my ninth problem is to solve a problem with a list
# # a list is a collection which is ordered and changeable. In python lists are written with sqaure brackets
# a list contain different data types
# a list can contain duplicate values
# a list can be nested
# a list can be accessed by index
# a list can be slices
# a list can be modified
# a list can be looped through
# a list can be sorted
# a list can be reversed
# a list can be copied
# a list can be cleared
# a list can be deleted
# a list can be joined
# a list can be multiplied
# a list can be unpacked
# a list can be used as a stack
# a list can be used as a queue
# a list can be used as a deque
# a list can be used a linked list
# a list can be used as a tree
# a list can be used as a graph
# a list can be used as a hash table
# a list can be used as a set
# a list can be used as a frozenset
# a list can be used as a dict
# a list can be used as a tuple
# a list can be used as a string
# a list can be used as a number
# a list can be used as a boolean
# a list can be used as a bytes
# a list can be used as a bytearray
# a list can be used as a memoryview
# a list can be used as a range
# a list can be used as a complex
mylist = ["apple", "banana"]
print(mylist)
mylist.append("cherry")
mylist.insert(1, "orange")
print(mylist)
mylist.remove("banana")
print(mylist)
mylist.pop()
print(mylist)
mylist.clear()
print(mylist)

# my tenth problem is to solve a problem with strings
name = "ravi"
print(name)

# my eleventh problem is to solve a problem with a dictionary
mydict = {"name": "ravi", "age": 25}
print(mydict)

# my twelveth problem is to solve a problem with a tuple
mytuple = ("apple", "banana", "cherry")
print(mytuple)

# my thrirteenth problem is to solve a problem with a set
myset = {"apple", "banana", "cherry"}
print(myset)


# give me a problem to solve with python programming language
# problem is to print the first 10 natural numbers using a loop
for i in range(1, 11):
    print(i)

# problem is to print the first 10 even numbers using a loop
for i in range(1, 21):
    if i % 2 == 0:
        print(i)

# problem is to print the first 13 odd numbers using a loop
for i in range(1, 26):
    if i % 2 != 0:
        print(i)

# problem is to print the first 10 natural numbers in reverse order using a loop
for i in range(10, 0, -1):
    print(i)

# problem is to print the first 10 even numbers in reverse order using a loop
for i in range(20, 0, -1):
    if i % 2 == 0:
        print(i)

# problem is to solve a mathematical problem with a loop
a = 10
b = 15
for i in range(1, 11):
    print(a + b)
    print(a - b)
    print(a * b)
    print(a / b)


# problem is to solve a problem with a function and a loop
def greet(name):
    return f"hello {name}, welcome to python programming"
names = ["ravi"]
for name in names:
    print(greet(name))

# problem is to solve with a list and a loop
mylist = ["Ravi"]
for item in mylist:
    print(item)

# problem is to solve with a dictionary and a loop
mydict: dict[str, int] = {"ravi": 25}
for key, value in mydict.items():
    print(f"my name is {key} and i am {value} years old")

# problem is to solve with a tuple and a loop
mytuple = ("apple", "Ravi",)
for item in mytuple:
    print(item)

# problem is to solve with a set and a loop
myset = {"Special Forces", "Ravi"}
for item in myset:
    print(item)

# problem is to solve with a string and a loop
name = "Ravi"
for char in name:
    print(char)

# problem is solve with a number and a loop
number = 10
for i in range(1, number + 2):
    print(i)

# problem is to solve with a boolean and a loop
is_ravi = True
for i in range(1, 12):
    if is_ravi:
        print("Ravi is here to solve problems with python programming language")

# problem is to solve with a bytes and a loop
mybytes = b"Ravi"
for byte in mybytes:
    print(byte)

# problem is to solve with a bytearray and a loop
mybytearray = bytearray(5)
for byte in mybytearray:
    print(byte)

# problem is to solve with a memoryview and a loop
mybytes = b"Ravi"
mybytearray = bytearray(mybytes)
memoryview = memoryview(mybytearray)
for byte in memoryview:
    print(byte)

# problem is to solve with a range and a loop
for i in range(1, 21):
    print(i)

# problem is to solve with a complex number and a loop
mycomplex = complex(2, 3)
for i in range(1, 21):
    print(mycomplex)

# problem is to solve with a if and else
number = 10
if number > 0:
    print("number is positive")
else:
    print("number is negative")

# solving problem with conditional statements such as if, elif and else
print("enter a number")
number = int(input())
if number > 0:
    print("number is positive")
elif number < 0:
    print("number is negative")
else:
    print("number is zero")

# problem is to solve with a nested if
print("enter a number")
number = int(input())
if number > 0:
    if number % 2 == 0:
        print("number is positive and even")
    else:
        print("number is positive and odd")
elif number < 0:
    if number % 2 == 0:
        print("number is negative and even")
    else:
        print("number is negative and odd") 