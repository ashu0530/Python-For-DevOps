'''
Raising Custom errors
In python, we can raise custom errors by using the raise keyword.

salary = int(input("Enter salary amount: "))
if not 2000 < salary < 5000:
    raise ValueError("Not a valid salary")

In the previous tutorial, we learned about different built-in exceptions in Python and why it is important to handle exceptions. 
However, sometimes we may need to create our own custom exceptions that serve our purpose.

Defining Custom Exceptions
In Python, we can define custom exceptions by creating a new class that is derived from the built-in Exception class.

Here's the syntax to define custom exceptions:

class CustomError(Exception):
  # code ...
  pass
try:
  # code ...
except CustomError:
  # code...

This is useful because sometimes we might want to do something when a particular exception is raised. For example, sending an error report to the admin, calling an api, etc.
'''

a = int(input("enter any value between 5 and 9: "))

if a < 5 or a > 9:
    raise ValueError ("Value should between 5 and 9")   #error give 


#defining custom errors

a = input("enter any value between 5 and 9: ")

try: 
    if a.lower() == "quit":
        exit()
    elif int(a) < int(5) or int(a) > int(9):
        raise ValueError ("value should between 5 and 9")
except Exception as e:
    print("program exit", e) 
