# a, b = 0, 1

# while a < 10:
#     print(a)
#     [a, b] = [b, a + b]

# x = 3
# y = 3.5
# x = y
# print(x)

# name = input("What's your name?")
# print("Hello, " + name)

# name = input("What is your name ")
# print("Hello,", name)

#numeric type

#######int
#number = 5

# #######float
# pointNum = 2.5

# #######complex
# comp = 2+3j
# print(type(comp))

# #string
# nameVar = 'Python Learning'
# print(type(nameVar))

# #boolean
# is_boy = True
# print(type(is_boy))

# #sequece type

# ####list
# listItems=[100,200,300]
# listItems=[400,500,600]     #list are mutable
# print(listItems)

# ####tuple
# tup1 = (1,2,3)      #immutable
# tup2 = (4,5,6)
# print(tup1, tup2)


# ####range
# rangeType = range (1, 6)
# print(rangeType)



# #mapping type

# ####dictionary

# details = {'name':'Abhishek', 'level':'bachelors', 'age':22}
# print(details)

# #set type

# ####set

# setvalues = {1,32,43,23,12,42,12}
# print(type(setvalues))


# #binary type

# ####bytes
# bytesTypeVar = bytes([2,5,7])
# print(bytesTypeVar)

# ####byteArray
# byteArrayTypeVar = bytearray([3,7,10])
# print(byteArrayTypeVar)


# #none type

# somethingIncluded = None
# print(type(somethingIncluded))

# age = int(input("Enter your age: "))
# age = age + 2
# print("your age is ",age)     #using a comma(,) for integer type (i.e, concatination is for sttring type only)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))    #typecasting
# print(num1 + num2)

# num3 = int('23')
# num4 = 3
# print(num3 + num4)

# a = 5
# b = int(3.54)
# print(a+b)

#print('i\'ll call you later')    #escape sequence uses

# numbe = 2 ** 3 ** 2   #exponent and it's associtavity is right to left
# print(numbe)

# print("Hello", "rahul",end=" ")
# print("Are you excited?")


# a = input("Enter your name: ")
# b = input("enter your age: ")
# print(a + "\t" + b)

# x = input("Enter first number: ")
# y = input("Enter second number: ")
# z = input("Enter third number: ")
# # print(x - y)
# print(int(x) ** int(y) ** int(z))

# a = '''
# iqwdjijwq
# wefjijewi
# eniwej
# kewniewn
# nwejn
# '''
# print(a[12])


####String Slicing
# fruit = "mango"
# print(fruit)

# nm = "Harry"
# print(nm[-4:-2])  # 1 : 3 including index 1 and 2 but not 3


#converting european elivator floors into us based floor system
#europe's 0 means ground floor is americans 1 floor which is he griund floor in US
# givenFloor = input("Enter the floor: ")
# converted = int(givenFloor) + 1
# print("The converted floor is: ", converted)


# #Get the name of the file and open it
# name = input("Enter file: ")
# handle = open(name, "r")

# #count word frequency
# counts = dict()
# for line in handle:
#     words = line.split()
#     for word in words:
#         counts[word] = counts.get(word, 0) + 1

# #Find the most common word
# bigCount = None
# bigWord = None
# for word, count in counts.items():
#     if bigCount is None or count > bigCount:
#         bigWord = word
#         bigCount = count


# #All done
# print(bigWord, bigCount)

# x = 1 + 2 * 3 - 8 / 4
# print(x)

# astr = "123"
# try :
#     astr = int(astr)
#     print(astr)
# except :
#     astr = -1

# print("This part runs", astr)

# x = 0
# if x < 2 :
#     print('Small')
# elif x < 10 :
#     print('Medium')
# else :
#     print('LARGE')
# print('All done')

# x = 2
# if x < 2 :
#     print('Below 2')
# elif x >= 2 :
#      print('Two or more')
# else :
#     print('Something else')


# astr = 'Hello Bob'
# istr = int(astr)
# print('First', istr)
# astr = '123'
# istr = int(astr)
# print('Second', istr)

# astr = 'Hello Bob'
# istr = 0
# try:
#     istr = int(astr)
# except:
#     istr = -1

# print(istr)

# x = 5
# print(type(x))
# x = ["apple", "banana", "cherry"]
# print(type(x))
# x = ("apple", "banana", "cherry")
# print(type(x))
# x = {"name" : "John", "age" : 36}
# print(type(x))

# a = [1,2,3]
# b = a[:]

# print(b,a)

# cars = 100
# print(f"space in a car is {cars}")

# big = max("Hello world")
# print(big)

# tiny = min("Hello world")
# print(tiny)

# a = 'Hello, World!'
# print(a[::2])

# def distance_from_zero(arg):
#     if type(arg) in (int, float):
#         return abs(arg)
#     else:
#         print("Not Possible")
# distance_from_zero(-10) and ("cat")

# x = 10
# y = 10
# print(x is y)
# print(id(x))
# print(id(y))

# a = "Hello"
# b = "Hello"
# print(a is b)

# c = 10
# print(c is x)

# list1 = [1, 2, 4]
# list2 = [1, 2, 4]
# print(list1 == list2)

# my_dict = {
#     "name": "Abhishek",
#     "class": 12,
#     "Address": "Arjundhara"
# }
# print(my_dict)

# a = 'Hello, World!'
# print(a[::-1])

# import math
# x = 'hello'
# y = 20
# print(math.factorial(x))

# def __new__(cls):
#     print("Hello")

# x, y = 3, 4
# y, z = 5, 6
# print(x + y + z)

