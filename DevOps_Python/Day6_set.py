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
s1 = {1,2,3,4,5}
s2 = {6,7,8}
print(s1.union(s2))   #union of both sets
print(s1,s2)     

s1.update(s2)
print(s1,s2)

#intersection of sets   -->common in both set
cities = {"berlin","delhi","varanasi"}
cities1={"kanpur","varanasi"}

ans=(cities.intersection(cities1))
print(ans)


#symmetric_difference
cities = {"tokyo","varanasi","berlin","delhi"}
cities2 = {"tokyo","varanasi","shanghai","kathmandu"}
print(cities.symmetric_difference(cities2))         


#asymmetric_difference
cities = {"tokyo","varanasi","berlin","delhi"}
cities2 = {"tokyo","varanasi","shanghai","kathmandu"}
print(cities.symmetric_difference_update(cities2))   


#difference and difference_update
cities = {"tokyo","varanasi","berlin","delhi"}
cities2 = {"tokyo","varanasi","shanghai","kathmandu"}
print(cities.difference(cities2))
print(cities2.difference(cities))

#isdisjoint and issuperset
cities = {"tokyo2","varanasi2","berlin","delhi"}
cities2 = {"tokyo","varanasi","shanghai","kathmandu"}
print(cities.isdisjoint(cities2))

cities = {"tokyo","varanasi","berlin","delhi"}
cities2 = {"tokyo","varanasi"}
print(cities.issuperset(cities2))

print(cities2.issubset(cities))


#add --> add single item in set
cities = {"tokyo2","varanasi2","berlin","delhi"}

(cities.add("kanpur"))
print(cities)

#update --> add multiple values in set
cities = {"tokyo2","varanasi2","berlin","delhi"}
cities2 = ("kanpur" , "gurugram")
cities.update(cities2)
print(cities)


#remove/discard
cities = {"tokyo2","varanasi2","berlin","delhi"}
cities.remove("tokyo2")   #can't handle error if tokyo2 is not present
print(cities)

cities = {"tokyo2","varanasi2","berlin","delhi"}
cities.discard("tokyo3")
print(cities)


#pop
cities = {"tokyo2","varanasi2","berlin","delhi"}
print(cities.pop())  #random pop the value 


#del method
# cities = {"tokyo2","varanasi2","berlin","delhi"}
# del cities
# print(cities)   #entire is set is deleted  so throw an error

cities = {"tokyo2","varanasi2","berlin","delhi"}
cities.clear()
print(cities)


#check item in sets
cities = {"tokyo2","varanasi2","berlin","delhi"}
if "tokyo2" in cities:
    print("tokyo2 exist")
else:
    print("tokyo2 not exist")


cities = {"tokyo2","varanasi2","berlin","delhi"}
for items in cities:
    if "tokyo2" in items:
        print("tokyo2 exist")
    else:
        print("tokyo2 not exist")