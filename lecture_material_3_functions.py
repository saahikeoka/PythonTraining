def prints_four():
    print("this")
    print("is")
    print("an")
    print("example")


prints_four()
prints_four()


def function_name():
    print(2+2)  # ident function code so that python reads it correctls

    # leave 2 blank lines before/after the function, python style guide practice
function_name()

number = int(input("Please enter a number:"))


def function_name(parameter):
    print(parameter+2) 


# passing an argument
function_name(number)
function_name(8)

# multiple parameters
first_str = "The number "


    # leave 2 blank lines before/after the function
def function_test_1(p1, p2, p3):
    print(p1 + str(p2) + p3)


function_test_1(first_str,5, " is an integer.") # parameters when defining the function, arguments when calling the function


def default_example(num1=7, num2=8): # when assigning default values, don't add spaces before/after = sign (opposed to when assigning values)
    print(num1 * num2)


default_example()       # using default values from the function
default_example(2)      # using default value for the 2nd argument
default_example(2, 3)   # not using default values


# using return, to use the result later
def default_example(num1=7, num2=8): # when assigning default values, don't add spaces before/after = sign (opposed to when assigning values)
    return num1 * num2


print(default_example() + 44)


# exercise 1
def hello_world_printer():
    print("Hello World")


hello_world_printer()

# exercise 2
name = input("What is your name?")


def name_printer(userName):
    print("Hello, " + userName)


name_printer(name)

# exercise 3
varLength = int(input("What is the Rectangular Prism's lenght? "))
varWidth = int(input("What is the Rectangular Prism's width? "))
varHeight = int(input("What is the Rectangular Prism's height? "))


def calculate_prism_volume(argLength, argWidth, argHeight):
    return argHeight * argLength * argWidth


total_volume = calculate_prism_volume(varLength, varWidth, varHeight)
print("The volume of the Rectangular Prism is " + str(total_volume))
# print("The volume of the Rectangular Prism is " + str(calculate_prism_volume(varLength, varWidth, varHeight)))     # alternative


# exercise 4
varCelsius = int(input("Please enter the temperature in Celsius: "))


def convert_to_Fahrenheit(argCelsius):
    return (18 * argCelsius + 320) /10
    # return round((1.8 * argCelsius + 32), 1)     # alternative


print("The Fahrenheit equivalent of " + str(varCelsius) + " degrees Celsius is " + str(convert_to_Fahrenheit(varCelsius)))

# modules contain set of functions, libraries
# generic import
import random   

print(random.randint(1, 10))    # need to type the module it's from 

# function import
from random import randint 

print(randint(1,20))    # no need to type the module it's from 

# universal import 
from random import *

print(randint(1,20))    # no need to type the module it's from, every function has been imported
print(random())

# exercise 5
from random import *
var_gas = randint(10, 25)                       # number of gallons of fuel that the car's fuel tank can hold
miles_with_full_tank = randint(200, 400)        # number of miles that the car can travel on a full tank


def miles_per_galon(var1, var2):                # calculates the MPG of the car assuming car manufacturers overestimates in their claims
    return var2 // var1

print("Gas fuel tank holds: " + str(var_gas))
print("Miles the car can travel with full tank: " + str(miles_with_full_tank))
print("The car can travel "+ str(miles_per_galon(var_gas, miles_with_full_tank)) + " miles per galon.")

# global and local scope
example = "hello world"             # global scope


def loc_ex():
    example = "this is a string"    # local scope
    return example


print(example)      # uses the global variable 
print(loc_ex())     # uses the variable from the function

# global variables can be accessed by code in a local scope
def print_glob():
    print(glob_var)


glob_var = "This is a string"   # ok to assign the value after the function, as long as the funcion call is after the assignment 
print_glob()


# you can use the same name for different variables as long as they are in different scopes
def loc_ex1():
    fruit = "pear"
    print(fruit)


def loc_ex2():
    fruit = "banana"
    print(fruit)


fruit = "apple"
loc_ex1()
loc_ex2()
print(fruit)


# assign a new value on a global variable in a local scope
def loc_ex():
    global fruit        # declare the local variable
    fruit = "pear"
    print(fruit)


fruit = "apple"
print(fruit)        # before reassignment
loc_ex()            # execute reassignment
print(fruit)        # after reassignemnt

