'''
Python Sets
Sets are unordered collection of data items. They store multiple items in a single variable. Set items are separated by commas and enclosed within curly brackets {}. 
Sets are unchangeable, meaning you cannot change items of the set once created. Sets do not contain duplicate items not repeated.
'''

s = {2,4,3,4}
print(s)
print(type(s))

info = {"Carlo",19,False,5.9,19}  #not ordered maintained
print(info)

emptyset = set()
print(type(emptyset))

emptyset = {()}
print(type(emptyset))


#Accessing the set items
info = {"Carlo",19,False,5.9,19}  
for item in info:
    print(item)


#methods of sets