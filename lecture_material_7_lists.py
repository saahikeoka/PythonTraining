example_list_1 = [5,4,3,2,1]
example_list_2 = [2.123, 4.34, 7.5]
example_list_3 = ["blue","green","red","yellow"]
example_list_4 = [True, False, True, True, False]
example_list_5 = [[5,4,3],[2,1],[6,7,8]]
example_list_5 = [[5,4,3],1,2,"blue",True, 5.3,"red"]

print(list("bla"))  # ['b', 'l', 'a']

checked_list = [1,2,3,4]

print(1 in checked_list)        # true
print(5 in checked_list)        # false
print(5 not in checked_list)    # true
print(1 not in checked_list)    # false

# exercise
ex_list_1 = [3, 2.1, True, "blue", [1,2,3]]
ex_list_2 = list("watermellon")

print("e" in ex_list_1)         # false
print("a" not in ex_list_2)     # false

# index 

index_example_1 = ["carpet", "hardwood", "linoleum"]
print(index_example_1[2])                   # "linoleum"

index_example_2 = [[5,4,3],[2,1],[6,7,8]]
print(index_example_2[0][1])                # "4" to access a value in a list within a list

print(index_example_1[0][2])                # "r" to access a iterable data within a list, but that isn't a list

negative_index = [1,2,3,4,5]
print(negative_index[-1])       # "5" access the last value from a list
print(negative_index[-2])       # "4" access the second to last value from a list

# using lists in operations as long as the datatype matches 
mixed_1 = [False, 365, 4.24, "this is a string"]

print(mixed_1[1] + 332) 
print(mixed_1[-1] + "and can be concatenated")

# list slice [inclusive : exclusive]
slice_example = [1,2,3,4,5,6,7,8,9]
print(slice_example[:4])       # [1, 2, 3, 4] until the 3rd position
print(slice_example[3:8])      # [4, 5, 6, 7, 8] from the 3rd position, until the 7th position
print(slice_example[6:])       # [7, 8, 9] from the 6th position onwards

# reassign a list item 
example = [2,4,6,8,0]
print(example)      # [2, 4, 6, 8, 0]

example[3] = 10
print(example)      # [2, 4, 6, 10, 0]

example[4:7] = [7,6,5]
print(example)      # [2, 4, 6, 10, 7, 6, 5]

# exercise
ex_list_3 = [[0, 2], [4, 6], [8, 10], [12, 14]]
print(ex_list_3[0][0])
print(ex_list_3[-1][-1])

ex_list_4 = ["chair", "table", "desk", "lamp", "bed"]
print(ex_list_4[-5])

print("Most people own at least " + str(ex_list_3[0][1]) + " " + ex_list_4[0]+"s.")
print("Most people own at least {} {}s.".format(str(ex_list_3[0][1]), ex_list_4[0]))

ex_list_5 = [0.98, 8.76, 6.54, 4.32]

print(ex_list_5[1:])    # [8.76, 6.54, 4.32]
print(ex_list_5[1:3])   # [8.76, 6.54]
print(ex_list_5[:2])    # [0.98, 8.76]

# del statements to remove item list
planets_del = ["pluto", "mars", "earth", "venus"]
del planets_del[0]             # removes an item based on an index
print(planets_del)

planets_remove = ["pluto", "mars", "earth", "venus"]
planets_remove.remove("pluto") # removes an item on the argument provided
print(planets_remove)

colors = ["blue", "red", "blue", "orange", "blue", "green", "blue"]
colors.remove("blue")          # remove only the first instance of that item 
print(colors)                  # ['red', 'blue', 'orange', 'blue', 'green', 'blue']

# append adds item to end of a list
pets_append = ["cat", "dog", "parrot"]
print(pets_append)             # ['cat', 'dog', 'parrot']
pets_append.append("fish")
print(pets_append)             # ['cat', 'dog', 'parrot', 'fish']

# insert allows items to be added anywhere on the list
pets_insert = ["cat", "dog", "parrot"]
print(pets_insert)             # ['cat', 'dog', 'parrot']
pets_insert.insert(1,"turtle")
print(pets_insert)             # ['cat', 'turtle', 'dog', 'parrot']

# sort allows a list that is made of all numbers or all strings to be sorted (ASCIIbetical order)
ex_sort_1 = [[12, 14], [0, 2], [8, 10], [4, 6]]
ex_sort_2 = [4,3,8,2,1,6,3]
ex_sort_3 = ['red', 'blue', 'orange', 'green']

ex_sort_1.sort()
ex_sort_2.sort()
ex_sort_3.sort()

print(ex_sort_1)            # [[0, 2], [4, 6], [8, 10], [12, 14]]
print(ex_sort_2)            # [1, 2, 3, 3, 4, 6, 8]
print(ex_sort_3)            # ['blue', 'green', 'orange', 'red']

ex_sort_1.sort(reverse=True)
ex_sort_2.sort(reverse=True)
ex_sort_3.sort(reverse=True)

print(ex_sort_1)            # [[12, 14], [8, 10], [4, 6], [0, 2]]
print(ex_sort_2)            # [8, 6, 4, 3, 3, 2, 1]
print(ex_sort_3)            # ['red', 'orange', 'green', 'blue']

ex_mixed = [False, 4.2, 0.9, True, -2]
ex_mixed.sort()
print(ex_mixed)             # [-2, False, 0.9, True, 4.2]; False = 0, True = 1

ex_ASCIIbetical = ["Andy", "kiwi", "apple", "Karen", "Brian", "banana"]
ex_ASCIIbetical.sort()
print(ex_ASCIIbetical)      # ['Andy', 'Brian', 'Karen', 'apple', 'banana', 'kiwi'] Uppercase strings comes first

ex_ASCIIbetical.sort(key=str.lower)     # forces the sort in alphabetical order
print(ex_ASCIIbetical)      # ['Andy', 'apple', 'banana', 'Brian', 'Karen', 'kiwi']

# index() statement
metals = ["copper", "gold", "silver", "iron"]
print(metals.index("silver"))       # "2" index

colors = ["blue", "red", "blue", "orange", "blue", "green", "blue"]
print(colors.index("blue"))         # "0" index, first index the argument was found

numbers = [4,3,2,1,0,1,2,3,4]
print(numbers.index(3))             # "3"

# pop() method removes and returns an item from a list
bands = ["Queen", "Led Zeppelin", "The Beatles", "MUSE", "Radiohead"]
end1 = bands.pop()       # removes the last item from a list

print(end1)              # "Radiohead"
print(bands)             # ['Queen', 'Led Zeppelin', 'The Beatles', 'MUSE']\

end2 = bands.pop(2)      # removes item with index 2
print(end2)              # "The Beatles"
print(bands)             # ['Queen', 'Led Zeppelin', 'MUSE']

# exercise 
arctic_animals = ["penguin", "elephant", "polar bear", "walrus", "tiger", "reindeer"]
del arctic_animals[4]
print(arctic_animals)           # ['penguin', 'elephant', 'polar bear', 'walrus', 'reindeer']

arctic_animals.remove("elephant")
print(arctic_animals)           # ['penguin', 'polar bear', 'walrus', 'reindeer']

arctic_animals.append("arctic fox")
print(arctic_animals)           # ['penguin', 'polar bear', 'walrus', 'reindeer', 'arctic fox']

arctic_animals.insert(2, "snowy owl")
print(arctic_animals)           # ['penguin', 'polar bear', 'snowy owl', 'walrus', 'reindeer', 'arctic fox']

arctic_animals.sort(key=str.lower)
print(arctic_animals)           # ['arctic fox', 'penguin', 'polar bear', 'reindeer', 'snowy owl', 'walrus']

print(arctic_animals.index("reindeer"))     # 3

print(arctic_animals.pop())     # walrus

# lists vs strings, both can be accessed by index 
# but lists are mutable, strings are immutable
# mutable datatypes are stored as references, so can have reference problems
ex_1 = [1,2,3]
ex_1[1] = 5
print(ex_1)       # [1, 5, 3]

ex_2 = "123"
# ex_2[1] = 5     # TypeError: 'str' object does not support item assignment
ex_2 = "153"      # instead, it has to be fully reassigned
print(ex_2)       # 153

ex_3 = "No, you can't"
ex_4 = "Yes" + ex_3[2:11] + "!"

print(ex_4)      # "Yes, you can!"

ex_5 = 3.14
ex_6 = ex_5
print(ex_6)      # 3.14

ex_9 = [1,2,3,4,5]
ex_10 = ex_9

ex_10[2] = 4
print(ex_9)         # [1, 2, 4, 4, 5]
print(ex_10)        # [1, 2, 4, 4, 5] both lists have been changed, because ex_9 and ex_10 both references the same list

# deepcopy() allows you to create a copy from a list instead of referencing the original list
import copy
ex_12 = [1,2,3,4,5]
ex_13 = copy.deepcopy(ex_12)

ex_13[2] = 4

print(ex_12)        # [1, 2, 3, 4, 5]
print(ex_13)        # [1, 2, 4, 4, 5], only ex_15 was modified

ex_15 = ["bush",
         "fern",
         "tree",
         "moss"]    # useful for lists with longer items, elements must be inline vertically to be compliant with PEP 8

print(ex_15)        # ['bush', 'fern', 'tree', 'moss']

# ex_16 = 2 + 4 + 1
ex_16 = 2 + \
        4 + \
        1       # use \ to brak line and align the elements vertically to be compliant

print(ex_16)    # 7

ex_17 = "The Emp\
re Strik\
es Back"        # for strings, the elements can't be aligned vertically, otherwise spaces would be added to the string

print(ex_17)    # "The Empre Strikes Back"

ex_18 = "hello " + \
        "world"  # if the string is concatenated expression, line it as you would in a math expression

print(ex_18)    # hello world