# lists
# * ordered
# * changable
# * dup allowed

empty_list = []
#print(empty_list)

a_list = ['text', 'another text', 'more text'] 
#print(a_list)

multiple_data_type_list = ['String', 15, 12.2, True]
# print(multiple_data_type_list)

name = 'karim'

year = 2022

good_mood = True


var_list = [name, year, good_mood]

#print(type(var_list))

#print(var_list)

soon = ('hi', 1, 15.5)

#print(f'{soon}\n{type(soon)}')

new_list = list(soon)

#print(f'{new_list}\n{type(new_list)}')

var = var_list[0]

var = var_list[-1]

var = var_list[0:2]


 
var = var_list[0:3:2]

var = var_list[:1]

var = var_list[1:]

if 'karim' in var_list:
    print('you are mentioned')



var_list[0] = 'ahmed'

var_list[0:2] = ['djamel', 2023]

var_list[1:2] = [8, 2001]

var_list[1:3] = [16]

var_list.insert(1, 2019)

var_list.append('object')

var_list2 = ['item1', 'item2']

var_list2 = ('11', 11)

var_list.extend(var_list2)

""" var_list.pop(5)

var_list.remove(11)

var_list.pop() """

del var_list[5]
#del var_list

var_list.clear()

# print(var_list)

var = len(var_list)


# print(var)

# Sets
a_set = {'first name', 'last name', 15, True}
an_set = {'word', 'python'}

print(a_set)
print(a_set)
# * Unordered
# * unchangable
# * dup not allowed
# * to access data use for loop or check if exist

a_set.add('added')  # math with python
a_set.update(an_set) # * dont have to be sets
 

thisset = {"apple", "banana", "cherry"}

x = thisset.pop()



"""
to remove data :
remove() rise error
discard() dont rise error
pop() remove last element cant know wich one 
clear() empty the set 
del remove the set
"""


# tuple
# * ordered
# * unchangable
# * dup  allowed
# * join via operator
a_tuple = ('data', 10, True)

# * to update a tuple change to a list then back to a tuple

# * unpacking
fruits = ("apple", "banana", "cherry", "strawberry", "raspberry")
#math with python
(green, yellow, *red) = fruits

print(green)
print(yellow)
print(red)

# * dictionaryext)}\n{type(fnumber)}\n{type(logic)}\n{multi_word_variable}')


#! exe:

# * ordered
# * changable
# * dup not allowed

""" Access data
dict[key]
get(key)
keys()
values()
items()

update data:

dict[]=
update({})

add data same

remove data: 
pop(key)
popitem()lastitem
del dict[key]
del # complete
clear()
"""

car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.values()

print(x)  # before the change

car["color"] = "white"

print(x)  # after the change
