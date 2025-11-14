'''
Sequences
 Sequences are a family of built-in types, including the list, tuple, range, string, and
 binary types. Sequences represent ordered and finite collections of items.
 Sequence operations.


List --> Ordered collection of data items, store multiple items in single variable, used as separated by commas and enclosed within square bracket []
List are mutable
 
'''

marks = [3,5,6,"ashu",True]   #different types of data types can be in list
print(marks)
print(type(marks))
print(marks[0],marks[1],marks[2],marks[3],marks[4])
print(len(marks))


#negative indexing
print(marks[-3])   #len-3

'''There are many operations that work across all of the types of sequences. We cover
 some of the most commonly used operations here.
 You can use the in and not in operators to test whether or not an item exists in a
 sequence:'''
#checking 
if 7 in marks:
    print("yes")
else:
    print("No")

if "ashu" in marks:
    print("ashu is there")
else:
    print("Not there")

#string
if "sh" in "ashu":
    print("Exist")
else:
    print("not exist")


print(marks)
print(marks[1:])


#jump index
print(marks[1:4:2])   #step 2


#list comprehension --> list comprehensions means on the fly we are creating lists
'''
list compresensions are used for creating new lists from other iterables like lists, tuples, dictionaries, sets, and even in arrays and strings.

syntax:

list = [Expression(item) for item in iterable if condition]
expression: it is the item which is being iterated
iterable: it can be list, tuple,dictionaries,sets and even arrays and strings
conditions: condition checks if the item should be added to the new list or not.
'''

lst = [i for i in range(4)]
print(lst)

names = ["ashu","cat","bruno","max"]
namewith_0=[item for item in names if "o" in item]
print(namewith_0)
morethan2length=[item for item in names if len(item)>3]
print(morethan2length)



#list methods
l = [1,2,0,9,3,3]
print(l)
l.append(7)  #added element in lists at last
#l.append("ashu")
print(l)

l.sort()
print(l)

l.reverse()
print(l)

print(l.index(2))

print(l.count(3))

m = l   #list reference
m[0] = 0
print(l)


list1 = [11,45,1,2,4,6,1,1]
print(list1)

#copy method
list2 = list1
list2=list1.copy()  #same as above
list2[0] = 0
print(list1)   #Original list is change because of reference 


list1.insert(1,199)  #insert value in list by specifying index
print(list1)

m = [900,1000,1100]
list1.extend(m)     #open list1 and put inside m at last
print(list1)  


k = list1+m
print(k)



#----------------------------------------------------------------Sequence-----------------------------------------------------------------------------------------------------
#You can use the in and not in operators to test whether or not an item exists in a sequence:
print(2 in [1,2,3]) #True

print('a' not in 'cat') #False

print(10 in range(12))  #True

print(10 not in range(2,4))

my_sequence = "Bill Cheatham"
print(my_sequence.index("a"))
print(my_sequence.index('a',9,12))

#The function list() can be used to create an empty list or a list based on another
#finite iterable object (such as another sequence):
print(list("Henry Miller"))

empty = []
nine = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
mixed = [0, 'a', empty, 'WheelHoss',nine]
print(mixed)
print(mixed[4][4])

#The contents of one list can be added to another using the extend method:
pies=['cherry', 'cream', 'apple', 'rhubarb']
desserts=["cookies","paste"]
desserts.extend(pies)
print(desserts)


'''
The most efficient and common way of removing the last item from a list and return‐
ing its value is to pop it. An index argument can be supplied to this method, removing
and returning the item at that index. This technique is less efficient, as the list needs
to be re-indexed:
'''

print(pies.pop())
print(pies)
print(pies.pop(1),pies)


#Removed method which remove first occurence of an item.
print(pies.remove('apple'),pies)


'''
One of the most potent and idiomatic Python features, list comprehensions, allows
you to use the functionality of a for loop in a single line. Let’s look at a simple exam‐
ple, starting with a for loop squaring all of the numbers from 0–9 and appending
them to a list:
'''

squares = []
for i in range(10):
    squares.append(i*i)
print(squares)

#list comprehension
squares2 = [i*i for i in range(10)]
print(squares2)


#Note that the functionality of the inner block is put first, followed by the for statement. You can also add conditionals to list comprehensions, filtering the results:

squares3 = [i*i for i in range(10) if i%2==0]
print(squares3)