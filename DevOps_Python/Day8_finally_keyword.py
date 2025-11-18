'''
Finally Clause
The finally code block is also a part of exception handling. When we handle exception using the try and except block, we can include a finally block at the end. 
The finally block is always executed, so it is generally used for doing the concluding tasks like closing file resources or closing database connection or may be 
ending the program execution with a delightful message.

Syntax:
try:
   #statements which could generate 
   #exception
except:
   #solution of generated exception
finally:
    #block of code which is going to 
    #execute in any situation

The finally block is executed irrespective of the outcome of try……except…..else blocks
One of the important use cases of finally block is in a function which returns a value.
'''

try:
    l = [1,5,6,7]
    i = int(input("Enter your index: "))
    print(l[i])
except:
    print("some error occured")

print("program execute successfully")   #why we can use same as finally same output is giving, but when we use as function

# finally:
#     print("program execute successfully")



def func1():
    try:
        l = [1,5,6,7]
        i = int(input("enter the index: "))
        print(l[i])
        return 1 #non error
    except:
        print("some error occured")
        return 0   #error
    finally:                                     #function returned always if return 0 or return 1
        print("I am always executed")

x = func1()
print(x)


try:
    num = int(input("Please enter the number integer: "))
except ValueError:
    print("Number entered is not integer")
else:
    print("integer accepted")
finally:
    print("this block is always executed")

