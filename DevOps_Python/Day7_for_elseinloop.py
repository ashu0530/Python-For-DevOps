#we can use else with for and while loop

'''
Python allows the else keyword to be used with the for and while loops too. The else block appears after the body of the loop. 
The statements in the else block will be executed after all iterations are completed. The program exits the loop only after the else block is executed.
'''

for i in range(5):
    print(i)     
else:               #If there is no control under loop then else execute so 0 to 4 goes then else execute
    print("No i")

for i in []:
    print(i)
else:
    print("yo")


for i in range(6):
    print(i)
    if i == 4:
        break    
else:       #no else execute coz it will break the loop .. so condition is loop should be finished not break if break then else will not execute.
    print("Sorry no i")

i= 0
while i<7:
    print(i)
    i = i+1
    if i == 4:
        continue
else:
    print("sorry no i")


for x in range(5):
    print(f"iteration no {x} in for loop {x+1}")
else:
    print("Else block in loop")
print("Out of loop")