#For loops can iterable over a sequence of iterable objects in python ex list, tuple,strings, dictionaries

name = "ashutosh"
for i in name:
    print(i,end=",")



name = "ashutosh"
for i in name:
    print(i,end=",")
    if i == 't':
        print("Ashutosh spelling have t character")

colours = ["Red", "green","Yellow","white"]
for colour in colours:
    print(colour)
    for i in colour:
        print(i)


#Range want to use for a loop for a specific number of times.
for k in range(5):
    print(k)


for i in range(1,9):
    print(i)

for k in range(1,20,2):
    print(k)


#----------------------------------------------------While loop -------------------------------------------------------------------------

#While loop execute statements while the condition is true, as soon as the condition becomes false, the interpreter comes out of the loop

i = 0
while (i<3):
    print(i)
    i+=1


# i = int(input("Enter the number: "))
# while (i<38):
#     i = int(input("Enter the second number: "))
#     print(i)
# print("Done with the loop")


#Decrementing while loop
count = 5
while (count > 0):
    print(count)
    count = count - 1


#Else with while loop
count = 5
while (count > 0):
    print(count)
    count = count - 1
else:
    print("I am inside else")

#Do while is not in python concept but we can do in python  do means instruction is happen whether is true of false


#break and continue statement in loops

#The break statement enables a program to skip over a part of thr code, a break statement terminates the very loop it lies within.

for i in range(1,101,1):
    print(i,end=" ")
    if i == 50:
        break
    else:
        print("continue till 50")
print("thankyou")


for i in range(12):
    print("5 X", i, "=", 5*i)
    if(i==10):
        break
print("Loop se bahar nikal gya")

#continue statement  is skipping the iteration
for i in range(12):
    if(i==10):
        print("Skip the iterations")
        continue
    print("5 X", i, "=", 5*i)
print("Loop se bahar nikal gya")


#Do while emulate
i=0 
while True:
    print(i)
    i+=1
    if (i%2== 0):
        break