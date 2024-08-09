value1 = "this is a String"
value2 = 'this is also a String!'
print(value1)
print(value2)

print(value1[2])    # 3rd index from the variable
print("apple"[0])   # 1st index from the variable

#string slice
value3 = "apricots"
print(value3[:3])   # until index 3, "apr"
print(value3[2:5])  # start at index 2, ends before 5th index, "ric"
print(value3[4:])   # start at index 4, "cots"

concat1 = "this is"
concat2 = "a concat"
print (concat1+" "+concat2)

concat3 = "R2"+"-"+"D2"
print(concat3)          # R2-D2
print(concat3[3])       # D
print(concat3[1:4])     # 2-D

unchanged = "forrest gump"
sliced = unchanged[6:]
print(sliced)
print(unchanged)
print(unchanged[10])
print(unchanged)    # not changed by accessing a index before

ex1 = "Just do it!"
print(ex1[10])
print(ex1[5:7])
print(ex1[8:])
print(ex1[:4])
print("don't"+" "+ex1[5:])

# type() finds the datatype
print(type("text")) # <class 'str'>
print(type(False))  # <class 'bool'>
print(type(2))      # <class 'int'>
print(type(1.2))    # <class 'float'>

# str() convert to a string
value4 = str(True)
value5 = str(5)
value6 = 2.1

print(type(value4)) # <class 'str'>
print(type(value5)) # <class 'str'>
print(type(value6)) # <class 'float'>

# escape sequences
print("This\tis\ta\tlot\tof\space.") # \t adds a ident sized space
print("Line one\nLine two") # \n new line
print("The movie is called \"Star Wars\"") #\' or \"
print("All scape sequences contain a \\")# \\ to add a backslash 

ex2 = 1.2
print(type(ex2))
print(str(ex2)+" is a float")
print('Hello, I\'m Cinthia, it\'s nice to meet you!')

print("*******\n *****\n  ***\n   *")

name = input("What is your name?")
print("Hello, "+name+".")
print(type(name))

age = input("How old are you?")
print("You are "+ age +" years old.")
print(type(age))

ex_name = input("What is your name?")
ex_quest = input("What is your quest?")
ex_color = input("What is your favorite color?")

print("So your name is "+ex_name+ ", your quest is "+ex_quest+", and you favorite color is "+ex_color+".")

age1 = int(input("How old are you?"))

print(type(age1))
print("So are " +str(age1)+ " years old.")

user_float = float(input("Please enter a float."))
print(type(user_float))

user_int = int(input("Please enter a number: "))
int_sum = user_int+10 

print ("Your value + 10 is " + str(int_sum))