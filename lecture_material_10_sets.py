# datatype of collection of items similar to list
# but can't have duplicate items and items are unordered

set_1 = {9,8,7,6}
set_2 = set({"a", "b", "c", "d", "e"})

print(set_1)        # {8, 9, 6, 7}
print(set_2)        # {'c', 'a', 'd', 'e', 'b'} , out of order

set_3 = {1,1,2}
print(set_3)        # {1, 2} if there are repeated items, they are ignored

set_4 = set({})     # to create an empty set, because using "set_4 = {}" will create a dictionary instead 

set_5 = set(range(1,12,2)) 
print(set_5)        # {1, 3, 5, 7, 9, 11}

set_6 = {"a", 3.14, True, 12}
print(set_6)        # {True, 3.14, 12, 'a'} can hold items from different datatypes

# items can not be accessed by index, can be accessed by for loop instead
set_7 = (3, 6, 9, 12, 15)

for num in set_7: 
    print(num)

# check if value exists in the set
print(12 in set_7)      # true
print(10 in set_7)      # false

olympic_cities = ["Athens","Paris","St.Louis","London","Stockholm","Berlin","Antwerp","Chamonix","Paris","St.Moritz","Amsterdam","LakePlacid",
                  "LosAngeles","Garmisch-Partenkirchen","Berlin","Sapporo","Garmisch-Partenkirchen","Tokyo","Helsinki","Cortinad'Ampezzo","London",
                  "St.Moritz","London","Oslo","Helsinki","Cortinad'Ampezzo","Melbourne","Stockholm","SquawValley","Rome","Innsbruck","Tokyo","Grenoble",
                  "MexicoCity","Sapporo","Munich","Innsbruck","Montreal","LakePlacid","Moscow","Sarajevo","LosAngeles","Calgary","Seoul","Albertville",
                  "Barcelona","Lillehammer","Atlanta","Nagano","Sydney","SaltLakeCity","Athens","Turin","Beijing","Vancouver","London","Sochi","RiodeJaneiro",
                  "Pyeongchang","Tokyo","Beijing","Paris","Milan Cortinad'Ampezzo","LosAngeles","FrenchAlps","Brisbane","SaltLakeCity"]

set_olympic_cities = set(olympic_cities)

print(set_olympic_cities)       # all the cities not repeated
                # {'Vancouver', "Cortinad'Ampezzo", 'Nagano', 'Athens', 'Amsterdam', 'Tokyo', 'SquawValley', 'Munich', 'Seoul', 'Atlanta', 'RiodeJaneiro', 
                # 'Lillehammer', 'SaltLakeCity', 'Chamonix', 'Helsinki', 'Berlin', 'Garmisch-Partenkirchen', 'Beijing', 'Calgary', 'Rome', 'Pyeongchang', 'Oslo', 
                # 'St.Moritz', 'St.Louis', 'Turin', 'Stockholm', 'LakePlacid', 'Brisbane', 'Barcelona', 'Grenoble', "Milan Cortinad'Ampezzo", 'Moscow', 'Melbourne', 
                # 'Paris', 'LosAngeles', 'Sarajevo', 'Antwerp', 'Sapporo', 'Sydney', 'FrenchAlps', 'Sochi', 'London', 'Albertville', 'Montreal', 'Innsbruck', 'MexicoCity'}

print(len(set_olympic_cities))      # 46
print(len(olympic_cities))          # 67

# methods
scifi = {"star track", "star wars", "halo"}

scifi.add("mass effect")
print(scifi)                # {'star track', 'mass effect', 'halo', 'star wars'} adds to the list

scifi.add("star wars")
print(scifi)                # {'star track', 'mass effect', 'halo', 'star wars'} no change if the value already exists

scifi.remove("star wars")
print(scifi)                # {'star track', 'mass effect', 'halo'} removes an item from the list, returns an error if it doesn't exists

scifi.discard("game")
print(scifi)                # {'star track', 'mass effect', 'halo'} same as remove, but if the item doesn't exits, it doesn't error out

scifi.clear()
print(scifi)                # set() everything from the set is removed

mountains  = {"Everest" , "Kilimanjaro", "Fuji"}
copy_mountains = mountains.copy()

print(copy_mountains is mountains)      # False
 
mountains.clear()
print(copy_mountains)       # copies the set with its own reference, so it's not affected by changes to the set it's copied from 
print(mountains)

set_8 = {1,2,3}
set_9 = {4,5,6}
set_10 = set_8.union(set_9)
set_11 = set_8 | set_9      # alternative to union

print(set_10)               # {1, 2, 3, 4, 5, 6}    
print(set_11)               # {1, 2, 3, 4, 5, 6}

set_12 = {4,5,6,7,8}
set_13 = {6,7,8,9,10}
set_14 = set_12.intersection(set_13)
set_15 = set_12 & set_13    # alternative to intersection

print(set_14)               # {8, 6, 7} return what items two sets have in common
print(set_15)               # {8, 6, 7}
print(type(set_14))

set_17 = set_13.difference(set_12)      # subtract a set from another, removes the intersection
set_16 = set_13 - set_12                # alternative to difference

print(set_16)               # {9, 10}
print(set_17)               # {9, 10}

# set comprehension
comp_1 = { even+2 for even in range(2, 11, 2)}          # range from 2 to 10, every 2. sum + 2 at the result
print(comp_1)               # {4, 6, 8, 10, 12}

comp_2 = {char.lower() for char in "ALLCAPS"}           # set contains all unique letters of "ALLCAPS" string, as lowercase          
print(comp_2)               # {'c', 'a', 'l', 's', 'p'}