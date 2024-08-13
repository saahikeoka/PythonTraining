# mutable datatype
# can store a collection of values like a list
# but instead of being assigned to a index, the items are assigned to keys

console = {"nintendo": "wii", "sony": "playstation", "microsoft": "xbox"} # key:value pairs

print(console["microsoft"])     # "xbox", access the values by the keys as you would on a list with indexes
val = console["microsoft"]      # values can also be assigned to values
print(val)
print("The " + console["sony"] + " 4 is the newest gaming console.")        # and be used in expressions

# dictionary keys can of other datatypes, including ints floats bools and mixed

mohs_hardness = {9:"corundum", 10:"diamond"}
floats = {1.23: 1000, 3.14159: 10000, 2.718:100000}
mixed = {"string": 1, 1023: 2, 4.902: 3, False: 4}

# unlike lists, dictionaries are unordered
print ([2,4,6] == [2,4,6])      # true
print ([2,4,6] == [6,4,2])      # false, same items, but not in the same order 

first = {0: 2.1, 1: 2.2, 2: 2.3, 3: 2.4}
second = {2: 2.3, 0: 2.1, 3: 2.4, 1: 2.2} 
print(first == second)          # true, same key:value pairs, order does not matter

# can check if a key exists with in and not in operators
print(0 in first)               # true if the key exists
print(4 not in first)           # true if the key doesn't exists in the dictionary

# exercise 
ex_dictionary = {1: "blue", 2: "red", 3: "green", 4: "yellow", 5: "purple"}
print(ex_dictionary[3])             # "green"
print(3 in ex_dictionary)           # true
print(1 not in ex_dictionary)       # false

# methods 
birth_years = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
print(birth_years.keys())       # "dict_keys([1994, 1969, 1982, 2000])" return all the keys from a dictionary      
print(birth_years.values())     # "dict_values(['bill', 'emily', 'elizabeth', 'turner'])" return all the values from a dictionary

for key in birth_years.keys():  # for method can be used to iterate through what is returned by it
    print(key)
    
for values in birth_years.values():
    print(values)

print(birth_years.items())      # "dict_items([(1994, 'bill'), (1969, 'emily'), (1982, 'elizabeth'), (2000, 'turner')])" 
                                # return a list of tuples (datatype), each tuples contains 2 items, being keys and items from a dictionary  

for key, value in birth_years.items():      # need to use 2 placeholder names in the for method, since there are 2 items in the result
    print(key, value)

print(type(birth_years.keys()))     # <class 'dict_keys'>
print(type(birth_years.values()))   # <class 'dict_values'>
print(type(birth_years.items()))    # <class 'dict_items'>

print(list(birth_years.keys()))     # [1994, 1969, 1982, 2000], converted from dict_keys datatype to list
print(list(birth_years.values()))   # ['bill', 'emily', 'elizabeth', 'turner'], converted from dict_values datatype to list
print(list(birth_years.items()))    # [(1994, 'bill'), (1969, 'emily'), (1982, 'elizabeth'), (2000, 'turner')], converted from dict_items datatype to list

print("elizabeth" in birth_years.values())      # true, to check if the value exists in the dictionary

# get() looks for and gets a key from a dictionary, and doesn't return an error when the key is not found 

# if 1974 in birth_years:
#     print(birth_years[1975])
# else:
#     print("1975 is not a key in birth_years.")

print(birth_years.get(1975, "1975 is not a key in birth_years."))   # first argument is the key to be looked for, and the second argument is what to be returned in case the key is not found

print(len(birth_years))             # 4, number of key:value pairs

# exercise
songs = {"Queen": "Bohemian Rhapsody", 
         "Bee Gees": "Stayin' Alive", 
         "U2": "One", 
         "Michael Jackson": "Billie Jean", 
         "The Beatles": "Hey Jude", 
         "Bob Dylan": "Like A Rolling Stone"}       # dictionaries can be lined vertically

print(len(songs))

for key in songs.keys():
    print(key)

print(songs.values())

for key, value in songs.items():
    print(key, value)

print(songs.get("Promise of the Real", "Promise of the Real is not a valid key."))

# fromkeys() needs to be used in an empty dictionary
# first argument must be an iterable item eg list or string, it will be the keys to the dictionary
# second argument can be any datatype, including a dictionary, it will be the value the fromkeys returns
ex_1 = {}.fromkeys(["address"], "1600 Pennsylvania Avenue NW")    

print(ex_1)             # {'address': '1600 Pennsylvania Avenue NW'}

ex_2 = {}.fromkeys("abc", "test")    
print(ex_2)             # {'a': 'test', 'b': 'test', 'c': 'test'}

ex_3 = {}.fromkeys("addr", "test")    
print(ex_3)             # {'a': 'test', 'd': 'test', 'r': 'test'} repeated key isnt created

ex_4 = {}.fromkeys(["brand"])    
print(ex_4)             # {'brand': None} None is used if the second argument isn't provided

# pop() method, same as for lists, but it must be provided an argument, since dictionaries aren't ordered, so the last item can't be removed by default
ex_5 = {"make": "Honda", "model": "civic", "year": 2016}

model = ex_5.pop("model")   # need to provide the key of the key:value pair thar will be removed
print(ex_5)         # {'make': 'Honda', 'year': 2016}
print(model)        # "civic"  

# popitem() removes the last item from a dictionary, it used on a version previous to Python 3.7, a random item will be removed
ex_6 = {"name": "bob", "age": 38, "occupation": "accountant", "workplace": "HR block"}
ex_6.popitem()
print(ex_6)         # {'name': 'bob', 'age': 38, 'occupation': 'accountant'}

# exercise 
ex_7 = {}.fromkeys("bcdfghjklmnpqrstvxzwy","consonant")

for key, value in ex_7.items():
    print(key, value)

fast_food_items = {"McDonald's": "Big Mac", "Burger King": "Whopper", "Chick-fil-A": "Original Chicken Sandwich"}

print(fast_food_items.pop("McDonald's"))
fast_food_items.popitem()
print(fast_food_items)

# clear() method removes everrthing from a dictionary

ex_7.clear()
print(ex_7)

# copy() returns an exact copy of a dictionary with its own reference
birth_years_2 = {1994: "bill", 1969: "emily", 1982: "elizabeth", 2000: "turner"}
people = birth_years_2.copy()
people[1982] = "madeline"

print(birth_years_2)    # {1994: 'bill', 1969: 'emily', 1982: 'elizabeth', 2000: 'turner'}
print(people)           # {1994: 'bill', 1969: 'emily', 1982: 'madeline', 2000: 'turner'}

# update() add key:value pairs from one dictionary to another or override values of existing keys with the values from another dictionary
city_info = {"country":"Canada", "provice": "Ontario", "city": "Toronto"}
population = {"population": 2930000}

city_info.update(population)       # {'country': 'Canada', 'provice': 'Ontario', 'city': 'Toronto', 'population': 2930000}
print(city_info)                   # copies population into city_info, with its own reference

population["population"] = 3000000
print(city_info)                   # not updated as it has its own reference

city_info.update(population)       # {'country': 'Canada', 'provice': 'Ontario', 'city': 'Toronto', 'population': 3000000}
print(city_info)                   # override the value of population as the key is the same

# exercise
internet_celebrities = {"DrDisrespect": "YouTube", "ZLaner": "Facebook", "Ninja": "Mixer"}
another_one = {"shroud": "Twitch"}

internet_celebrities.update(another_one)

new_internet_celebrities = internet_celebrities.copy()
internet_celebrities.clear()

print(internet_celebrities)
print(new_internet_celebrities)

# setdefault() method set values to keys if they are not found in the dictionary, without getting an error
computers = {"google": "chromebook", "apple": "macbook", "microsoft": "surface pro" }

# if "Lenovo" not in computers: 
#     computers["Lenovo"] = "Thinkpad"

# print (computers)

computers.setdefault("Lenovo", "Thinkpad") # first argument is the key, the second is the value, if the key is not found
print (computers)

computers.setdefault("Lenovo", "Ideapad") # if the key exists, the value will not be updated to the value on the setdefault() method
print (computers)

# dict() alternative way of creating a dictionary
empty = dict()
print(empty)

with_values = dict(a=1, b=2, c=3)   # keys can't be bool, can't contain punctiations and special chars and can't begin with numbers
print(with_values)                  # {'a': 1, 'b': 2, 'c': 3}

with_values_2 = dict(a1=1, b_=2, c_3="ab")   # keys can't be bool, can't contain punctiations and special chars and can't begin with numbers
print(with_values_2)                # {'a1': 1, 'b_': 2, 'c_3': 'ab'}