# # can store a collection of values like a list
# # but instead of being assigned to a index, the items are assigned to keys

# console = {"nintendo": "wii", "sony": "playstation", "microsoft": "xbox"} # key:value pairs

# print(console["microsoft"])     # "xbox", access the values by the keys as you would on a list with indexes
# val = console["microsoft"]      # values can also be assigned to values
# print(val)
# print("The " + console["sony"] + " 4 is the newest gaming console.")        # and be used in expressions

# # dictionary keys can of other datatypes, including ints floats bools and mixed

# mohs_hardness = {9:"corundum", 10:"diamond"}
# floats = {1.23: 1000, 3.14159: 10000, 2.718:100000}
# mixed = {"string": 1, 1023: 2, 4.902: 3, False: 4}

# # unlike lists, dictionaries are unordered
# print ([2,4,6] == [2,4,6])      # true
# print ([2,4,6] == [6,4,2])      # false, same items, but not in the same order 

# first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
# second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2} 
# print(first == second)          # true, same key:value pairs, order does not matter

# # can check if a key exists with in and not in operators
# print(0 in first)               # true if the key exists
# print(4 not in first)           # true if the key doesn't exists in the dictionary

# exercise 