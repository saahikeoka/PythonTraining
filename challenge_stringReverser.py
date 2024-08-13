user_string = input("Please enter a string: ")
reverse = ""

for letter in range(len(user_string)-1, -1, -1): 
    reverse += user_string[letter]

print (reverse)