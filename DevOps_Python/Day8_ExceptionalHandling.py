'''
Exception handling is the process of responding to unwanted or unexpected events when a computer program runs. Exception handling deals with these events to a
void the program or system crashing, and without this process, exceptions would disrupt the normal operation of a program.

Exceptions in Python
Python has many built-in exceptions that are raised when your program encounters an error (something in the program goes wrong).

When these exceptions occur, the Python interpreter stops the current process and passes it to the calling process until it is handled. If not handled, the program will crash.

Python try...except
try….. except blocks are used in python to handle errors and exceptions. The code in try block runs when there is no error. If the try block catches the error, then the except block is executed.

Syntax:
try:
     #statements which could generate 
     #exception
except:
     #Soloution of generated exception

     
useful in server error handling 
'''

a = input("Enter the number: ")    #type ashu then program break coz of data type
print(f"Multiplication table of {a} is: ")
for i in range(1,11):
    print(f"{int(a)} X {i} = {int(a)*i}")


print("some lines of code")    #important code so program should run if input goes wrong then program break so there is no gurantee user give right input so i have to make program handle error if error occurs then some thing happen
print("End of program")



a = input("Enter the number: ")
print(f"Multiplication of table{a} is: ")

try:
    for i in range(1,11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except:
    print("Invalid input")

print ("some other codes")       
print("end of program")

#Value error  handling types of error when to use.

try:
    num = int(input("Enter the integer: "))
    a = [6,3]
    print(a[num])
except ValueError:                                #
    print("Number entered is not an integer")
except IndexError:
    print("index error")



name = input("Enter your name: ")
try:
    if name.isalpha() or name.islower():
        print(f"name is : {name}")
    raise ValueError
except ValueError as e:
    print(f"Name is not small letter as well as under alphabet: {e}")

print("Some code")


'''
 Exceptions are a type of error causing your program to crash if not handled (caught).
 Catching them with a try-except block allows the program to continue. These
 blocks are created by indenting the block in which the exception might be raised,
 putting a try statement before it and an except statement after it, followed by a code
 block that should run when the error occurs:


 There are many built-in exceptions, such as IOError, KeyError, and ImportError.
 Many third-party packages also define their own exception classes. They indicate that
 something has gone very wrong, so it only pays to catch them if you are confident
 that the problem won’t be fatal to your software. You can specify explicitly which
 exception type you will catch. Ideally, you should catch the exact exception type (in
 our example, this was the exception IndexError).
'''
thinkers = ['plato', 'palydo', 'gumpy']
while True:
    try:
        thinker = thinkers.pop()
        print(thinker)
    except IndexError as e:
        print(f"We tried pop too many thinkers {e}")
        break


thinkers = ['plato', 'palydo', 'gumpy']

try:
    for i in thinkers:
        ans = thinkers.pop()
        print(ans)
except IndexError as e:
    print(f"not having value")
print("some code")