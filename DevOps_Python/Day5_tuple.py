#Tuple are ordered collection of data items. They store multiple items in a single variable. Tuple items are separated by commas and enclosed with round brackets {}
#Tuples are unchangeable meaning we cannot alter them after creation.




tup = (1,4,5)
print(type(tup),tup )

tup = (1)
tup2 = (1,)
print(type(tup),type(tup2),tup2,tup)   #take as int because we have to give comma for tuple



tup = (1,4,5,"green",True)
print(type(tup),tup )
print(tup[0],tup[1],tup[2])

if 342 in tup:
    print("Yes it is present")
else:
    print("not present")


#slicing return new tuple 
tup2 = tup[1:3]
print(tup2)



#Methods in tuple
