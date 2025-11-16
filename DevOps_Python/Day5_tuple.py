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



#Methods in tuple  --> in tuples you can't directly change like add, remove we have to copy tuple in list change in list and copy in another tuple
countries = ("INDIA","ITALY","England","Spain")
temp = list(countries)
temp.append("Russia") #Add item
temp.pop(3)
temp[2] = "Finland"
countries = tuple(temp)
print(countries)


#Concatenate two tuples without converting them to list
countries=("INDIA","Afganistan","Bangladesh","Srilanka")
countries2=("America","Canada","France")
AsiaEurope=countries+countries2
print(AsiaEurope)


tuple1 = (0,1,2,3,2,3,4,1,1)
res = tuple1.count(3)
print("Count of 3 in tuple1 is:", res)
print("Index of 3 in tuple: ", tuple1.index(4))
print("Starting and ending till 3 to 8 index is: ", tuple1.index(4,4,8) )   #4:8 slicing
print("length:", len(tuple1))