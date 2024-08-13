# # string methods
# all_lower = "hello"
# all_upper = "HELLO!"

# print("hello".upper())
# print(all_lower.upper())

# print(all_upper.lower())        # this doesn't modify the string, if the change is needed, reassign the new value
# print(all_upper)

# print(all_upper.islower())      # false
# print(all_upper.isupper())      # true

# print("".isupper())             # false
# print("23%.,?\"".islower())     # false, there must be at least one letter for it to be true

# print(all_upper.lower().isupper())  # false

# print("text".isalpha())         # true, for letters only
# print("123a".isalnum())         # true, for numbers and letters only
# print("123".isdecimal())        # true, for numbers only
# print(" ".isspace())            # true, for spaces only
# print("Title Case!".istitle())   # true, for title case only - first letter capitalized, works with special charactes

# # none work on empty string

# print("".isalpha())                     # false
# print("hello world".isalpha())          # false, can't contain spaces
# print("hello 2".isalnum())              # false, can't contain spaces   
# print("hello!".isalpha())               # false, can't contain special characters including ponctuation   
# print("not just spaces"[3].isspace())   # true

# print("ABC".startswith("A"))                # true
# print("abc".startswith("A"))                # false, it's case sensitive
# print("Hello!".endswith("!"))               # true
# print("Hello World!".startswith("Hello"))   # true

# print("".join(["one", "two", "three"]))       # onetwothree
# print("Hello ".join(["World", "!"]))          # WorldHello !
# print("1".join(["2", "3", "4", "5"]))         # 2131415
# print(" ".join(["one", "two", "three"]))      # one two three
# print(", ".join(["one", "two", "three"]))     # one, two, three
# print("...".join(["one", "two", "three"]))    # one...two...three

# print("Eggs, Milk, Waffles, Bacon".split())         # by default, the separator is a space ['Eggs,', 'Milk,', 'Waffles,', 'Bacon']
# print("Eggs, Milk, Waffles, Bacon".split(", "))     # using ", " as separator ['Eggs', 'Milk', 'Waffles', 'Bacon']

# # exercise
# mixed_case = "A Song of Ice and Fire"

# print(mixed_case.isupper())
# print(mixed_case.islower())
# print(mixed_case.upper())
# print(mixed_case.lower())
# print(mixed_case.istitle())
# title_case = mixed_case.title()
# print(title_case)
# print(mixed_case.startswith("A"))
# print(mixed_case.endswith("Fire"))
# words = mixed_case.split()
# print(words)
# print(" ".join(words).isalpha())

# # rjust() ljust()
# print("Hello World".rjust(15))          # total length of the string "    Hello World"
# print("Hello World".ljust(15) + ".")    # total length of the string "Hello World    ."

# print("Hello World".rjust(15, "-"))          # "----Hello World"
# print("Hello World".ljust(15, "a") + ".")    # "Hello Worldaaaa."

# print("Hello World".center(15))              # "  Hello World  " 
# print("Hello World".center(15, ":"))         # "::Hello World::" 

# # strip() lstrip() lstrip() replace()
# print("   Hello World   ".strip())              # "Hello World" trim on both sides
# print("   Hello World   ".lstrip())             # "Hello World   " left trim
# print("   Hello World   ".rstrip())             # "   Hello World" right trim
# print("Hello World".strip("World"))             # "Hello" can trim other characters othen than spaces
# print("Hello World".strip(" World"))            # "He" it stops once it finds a character that is not included on the string list to be trimmed
# print("abcdef gh ijk lmn".rstrip(" amnkl"))     # "abcdef gh ij" the string list doesn't need to be in the same order 

# # print("Good Morning".replace("Morning", "Afternoon"))   # "Good Afternoon"

# # exercise 
# the_string = "North Dakota"
# print(the_string.rjust(17))
# print(the_string.ljust(17, "*"))
# center_plus = the_string.center(16, "+")
# print(center_plus)
# print(the_string.lstrip("North"))
# print(center_plus.rstrip("+"))
# print(center_plus.strip("+"))
# print(the_string.replace("North", "South"))

# # len() gets the length of an iterable type, such as string

# print(len("   Hello World!"))                       # 15, includes spaces, pontuation and special chars
# print("this"+" "+"is"+" "+"a"+" "+"string")         # "this is a string"
# print(len("this"+" "+"is"+" "+"a"+" "+"string"))    # 16
# print("antidisestablishmentarianism"[7:20])         # "establishment"
# print(len("antidisestablishmentarianism"[7:20]))    # 13

# format() 
name = input("What is the applicant's name: ")
degree = input("What did they major in at college? ")
job = input("What is their current occupation? ")
experience = input("How many years have they been working in their field? ")

print(name + " majored in " + degree + ", works as a " + job + " and has " + experience + " years of experience.")

print("{} majored in {}, works as a {} and has {} years of experience.".format(name, degree, job, experience))