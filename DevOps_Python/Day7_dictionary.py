#Dictionary 
'''
Dictionaries are ordered collection of data items after 3.7 version of python. They store multiple items in a single variable. Dictionary items are key-value pairs that are separated by commas and
enclosed within curly brackets {}.
'''

dic = {"ashu": "human","tota":"parrot"}
print(dic["tota"])

info = {"name": "ashu", "age":27, 'eligible': True}
print(info)
print(type(info))

#accessing single value
print(info['name'],info["age"])  #throw error if not exist
print(info.get('eligible'))    #error handle if not exist return none

#all keys accessible
print(info.keys())

for key in info.keys():
    #print(key)    #print(only key)
    print(f"{key} : {info[key]}")


print(info.items())
for key in info.items():
    print(key)

for key, value in info.items():
    print(f"The corresponding value to the key {key} is {value}")


#-------------------------------------------------------------------------Dictiornary methods------------------------------------------------------------------------
emp = {122: 45, 123: 56, 124: 88}
emp2 = {221: 80, 222: 76}
emp2.update(emp)
print(emp2)    #updating the values 

emp.clear()
print(emp)

emp = {}  
print(emp)  #empty dictionary

emp = {122: 45, 123: 56, 124: 88}
print(emp.pop(122))
print(emp)


#popitem clear last item in dict
emp = {122: 45, 123: 56, 124: 88}
print(emp.popitem())
print(emp)

#del keyword
emp = {122: 45, 123: 56, 124: 88}
# del emp
# print(emp)
del emp[122]
print(emp)

emp = {122: 45, 123: 56, 124: 88}
emp.update({125:22})
print(emp)




'''
A dict is a mapping of keys to values. The lookup of any particular value using a key is
 highly efficient and fast. The keys can be strings, numbers, custom objects, or any
 other nonmutable type

 A mutable object is one whose contents can change in place. Lists
 are a primary example; the contents of the list can change without
 the list’s identity changing. Strings are not mutable. You create a
 new string each time you change the contents of an existing one.
'''
map = dict()
print(type(map))

kv_list = [['key-1', 'value1'], ['key-2', 'value-2']]
print(type(kv_list))  #list
print(dict(kv_list)) #convert in dictionary

'''You can use the same syntax to set a value. If the key is not in the dict, it adds as a
 new entry. If it already exists, the value changes to the new value:'''
map = {'key-1': 'value-1', 'key-2': 'value-2'}
print(map)
print( map['key-1'])

map['key-3'] = 'value-3'
print(map)

map['key-1'] = 12
print(map)

if 'key-4' in map:
    print(map['key-4'])
else:
    print("not exist")

''' A more intuitive solution is to use the get() method. If you have not defined a key in
 a dict, it returns a supplied default value. If you have not supplied a default value, it
 returns None: 
 '''

print(map.get('key-4', 'default-value'))

#Use del to remove a key-value pair from a dict:
del (map['key-1'])
print(map)

print(map.keys())
print(map.values())
print(map.items())

for key, value in map.items():
    print(f"{key}, {value}")

'''
Similar to list comprehensions, dict comprehensions are one-line statements return
ing a dict by iterating through a sequence:
'''
letter = 'abcde'
cap_man =  {x: x.upper() for x in letter}
print(cap_man)
print(cap_man['b'])
