number1 = int(input("Please enter a positive integer: "))
sum_of_numbers = 0

init_number = number1

while number1 > 0:
    sum_of_numbers += number1       # sum_of_numbers = sum_of_numbers + number1
    number1 -= 1

print("The number you entered is: " + str(init_number))
print("The sum of the numbers is: " + str(sum_of_numbers))