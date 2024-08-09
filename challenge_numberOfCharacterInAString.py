value1 = input("Please enter a string: ")
counter = 0 

for letter in value1:
    counter += 1

print("The string entered is: " + value1)
print("It contains " + str(counter) + " letters.")