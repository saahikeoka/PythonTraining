counter = 0 

while counter < 3:
    print("something")
    counter += 1            # counter = counter + 1

# be careful with infinite loops

counter1 = 10

while counter1 != 0:
    print(counter1)
    counter1 -= 1

# FOR controlled by a fixed number of iterations, rather than a condition

word = "house"

for letter in word:
    print(letter)

# exercise    
word1 = "hello world"

for letter in word1:
    print(letter)

# range() returns a sequence of numbers, usually used to iterate over with FOR loop

one_input = range(5) # start at 0, increment by 1, until one less than the argument is reached

for num in one_input:
    print(num)

two_inputs = range(5, 10) # starts at the first argument, increment by 1, until one less than the second argument is reached

for num in two_inputs:
    print(num)

three_inputs = range(1, 20, 3) # starts at the first argument, until one less than the second argument is reached, incremented by the third argument 

for num in three_inputs:
    print(num)

three_inputs1 = range(20, 1, -3) # increment can be negative

for num in three_inputs1:
    print(num)