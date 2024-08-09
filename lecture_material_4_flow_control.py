# most basic flow control statement is the IF statement

# comparison operators > < <= >= != ==, results in true or false
print(4 > 3)                # true
print(1 > 3)                # false
print(9 >= 9)               # true
print (1 <= 2)              # true
print("Hello" == "hello")   # false
print(4.0 == 4)             # true

# AND OR operators
print(4 < 1 and "word" == "word")   # false
print(4 > 1 or "word" == "word")    # true

# NOT operator
print(not 6482 > 0)                 # not true = false
print(not "Python" != "Python")     # not false = true

# IF statement
# if True: 
#     "do stuff here"

veg = input("Type the name of a vegetable: ")

if veg == "corn":
    print("The vegetable is Corn.")
else:
    print("The vegetable is not Corn.")

# nested if and else statement
gpa = float(input("What was the applicant's grade point average "))
instituition = input("Is the student going to be educated at an approved institution?")

if gpa >= 3.7:
    if instituition == "yes":
        print("The application qualifies for a low APR student loan.")
    else:
        print("The application does not qualify since they have not been accepted into an approved institution.")
else:
    print("The applican't did not have a high enough grade to qualify.")

# elif else+if
veg = input("Type the name of a vegetable: ")

if veg == "corn":
    print("The vegetable is Corn.")
elif veg == "lettuce":
    print("The vegetable is Lettuce.")
else:
    print("The vegetable is not Corn or Lettuce.")

user_num = int(input("Please enter an integer: "))

if user_num < 0:
    print("The number you entered is less than 0")
elif user_num == 0:
    print("The number you entered is zero")
elif 0 < user_num <= 100:
    print("The number you entered is between 1 and 100")
else:
    print("The number you entered is greater than 100")

# truthy and falsey
string_example = input("Enter any string othen than empty one. ")

if string_example:  # works, but not a good practice
    print("Thank you for entering a string.")   # if not empty, truthy
else:
    print("You did not enter a string.")        # if empty, falsey

# string empty, int 0, float 0.0 is falsey values
print(bool(0))      # false
print(bool(1))      # true
print(bool(0.0))    # false
print(bool(0.2))    # true
print(bool(""))     # false
print(bool("a"))    # true


