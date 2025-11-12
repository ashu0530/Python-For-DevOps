names = "ashutosh"
print(len(names))

print(names[0:3])   #0 to n-1


fruits = "mango"
print(fruits, "is lenth of ", len(fruits))

print(fruits[0:4])
print(fruits[:4])
print(fruits[1:4])
print(fruits[:])  #take last full

#negative slicing
print(fruits[0:-3])  #0:len(fruits)-3
print(fruits[-1:-3])   
print(fruits[-3:-1])  #start from 0 to n-1 #ng including 0 not 4


#loop through using string
alphabets = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
for i in alphabets:
    print(i)

#Quiz
nm = "harry"
print(nm[-4:-2])   #1:3  --> ar