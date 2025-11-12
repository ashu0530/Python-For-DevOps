#Variables  add strings in variable
''' Python variables use dynamic typing. In practice, this means that they can be reas
signed to values of different types or classes: the same variable is set to a string, a number, and a dictionary. Variables can be
 reassigned to values of any type. '''
dog_name = 'spot' 
print(dog_name)

dog_name = 't-' + dog_name
print(dog_name)

big = 'large'
print(big)
big = 100*100
print(big)
big = {}
print(big)
big = []
print(big)



#Range function range() constructor, an object representing a sequence of numbers is returned  3 arguments --> starting,ending,steps

a=range(10)
b=list(range(20))
c=list(range(5,10))
print(a,b,c)



#Execution control
''' if/elif/else
 if/elif/else statements are common ways to branch between decisions in code'''

i = 76
if i == 45:
    print('i is 45')
elif i == 35:
    print('i is 35')
else:
    print("i don\'t know much about i...")


#nested if conditions used also in and if else statement

cat = 'pot'
if 's' in cat:
    print("Found an 's' in a cat")
    if cat == 'sheba':
        print("I found sheba")
    else:
        print("Some other cat")
else:
    print("A cat without 's' ")


'''For loop allow you to repeat a block of statements (a code block) once for each
member of a sequence (ordered group of items). As you iterate through the sequence,
the current item can be accessed by the code block'''

for i in range(20):
    x = i*20
    print(x)

#continue statement skip a step in a loop, jumping to the next item in the sequence.

for i in range(6):
    if i == 3:     #3 is skipped
        continue
    print(i)

#while loops repeat a block as long as a condition evaluates to True:

'''
It is essential to define a way for your loop to end. Otherwise, you will be stuck in the
loop until your program crashes. One way to handle this is to define your conditional
statement such that it eventually evaluates to False. An alternative pattern uses the
break statement to exit a loop using a nested conditional:
'''
count = 0 
while count < 3:
    print(f"The count is {count}")     
    count +=1


count = 0
while True:
    print(f"The count is {count}")
    if count > 3:
        break
    count +=1