# datatype made of a collection of items 
# enclosed in parentesis
# similar to lists, but it's immutable (can't be changed)

tuple_1 = ("a", "b", "c")
tuple_2 = (2.42, False, [1,2,3])
tuple_3 = (1,2,3,4,5,6,7,8,9,10)
tuple_4 = tuple([3.14, 2.205, 10])          # can be creted using the tuple() function, the argument should be a list or string, that 
tuple_5 = tuple("asdef")

print(tuple_4)                              # (3.14, 2.205, 10)
print(tuple_5)                              # ('a', 's', 'd', 'e', 'f')

tuple_7 = tuple({"a": 1, "b": 3, "c": 3})

print(tuple_7)                              # ('a', 'b', 'c') only the keys of a dictionary are used on the tuple

print(tuple_3[2])                           # each item has an idex, just like in a list, so it can be accessed by index or slice
print(tuple_3[:8])                          # for slices, the result is a tuple
print(tuple_3[:8])
print(tuple_3[2:7])
print(tuple_3[3:])
print(type(tuple_3[:8]))                    # <class 'tuple'>

# imutable, useful for collection of data that can't be changed (eg days of week, seasons and letters of the alphabet)
# it also takes less space in memory
# tuple_3[0] = "a"                            # TypeError: 'tuple' object does not support item assignment

tuple_8 = ("Fall", "Winter", 
           "Spring", "Summer")      # align vertically when it's across multiple lines

tuple_9 = (1,3,5)
list_1 = [1,3,5]

print(tuple_9.__sizeof__())         # 48 bytes
print(list_1.__sizeof__())          # 72 bytes

# other useful scenario for tuples is as a key in a dictionary
occupations = {("Angus","Young"): "musician",
               ("Narendra", "Modi"): "prime minister",
               ("Richard", "Branson"): "entrepeneur", 
               ("Quentin", "Tarantino"): "filmmaker"}           # {{lastname, firstname}: occupation}

seven_wonders = {("29°58'45.03″N", "31°08'03.69″E"): "Great Pyramid of Giza, Egypt",
                ("32.5355°N", "44.4275°E"): "Hanging Gardens of Babylon, Iraq",
                ("37°38'16.3″N", "21°37'48″E"): "Statue of Zeus at Olympia, Greece",
                ("37°56'59″N", "27°21'50″E"): "Temple of Artemis at Ephesus, Turkey",
                ("37.0379°N", "27.4241°E"): "Mausoleum at Halicarnassus, Turkey",
                ("36°27'04″N", "28°13'40″E"): "Colossus of Rhodes, Greece",
                ("31°12'50″N", "29°53'08″E"): "Lighthouse of Alexandria, Egypt"}

# tuple loop
major_cities = ("Tokyo", "London", "New York", "Shanghai", "Sydney")

for city in major_cities: 
    print(city)

count = 0
while count < len(major_cities): 
    print(major_cities[count])
    count += 1

backwards = len(major_cities) - 1
while backwards >= 0: 
    print(major_cities[backwards])
    backwards -= 1

# slicing with step
ints = (1,2,3,4,5,6,7,8,9,10)       # slice[start : end : step)

print(ints[::3])            # (1, 4, 7, 10) stride length of 3 - from start to end (not provided), every 3 indexes: index 0, 3, 6 and 9               
print(ints[1::2])           # (2, 4, 6, 8, 10) evens only - from index 1, to the end, access every other number
print(ints[7::-1])          # (8, 7, 6, 5, 4, 3, 2, 1) backwards from 8 - start at index 7 until the beginning, every -1 number
print(ints[8::-2])          # (9, 7, 5, 3, 1) odds only backwars - starts at the index 8 until the beginning, every -2 numbers

# count()
nested = (1,2,3, (4,5,6), (7,8,9), (10,11,12))

print(nested[4])                    # (7, 8, 9)
print(nested[4][1])                 # 8, to access an item in a tuple within a tuple

print(nested.count(1))              # 0, number of occurences of the provided argument
print(nested.count((4,5,6)))        # 1

repeat = (7,3,3,3,0,0,7,0,0)

print(repeat.count(7))              # 2
print(repeat.count(3))              # 3
print(repeat.count(0))              # 4

# index()
ints_2 = (1, 1, 7)

print(ints_2.index(7))              # 2, returns the index of the value provided on the argument
print(ints_2.index(1))              # 0, if repeated, returns on the first occurence

colors = ("blue", "red", "blue", "orange", "blue", "green", "blue")

print(colors.index("blue")) 
print(colors.count("blue")) 