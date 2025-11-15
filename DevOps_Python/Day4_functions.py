'''

a function is a mechanism for encapsulating a block of code. You
can repeat the behavior of this block in multiple spots without having to duplicate the
code. Your code will be better organized, more testable, maintainable, and easier to
understand.

Anatomy of a Function
The first line of a function definition starts with the keyword def, followed by the
function name, function parameters enclosed in parentheses, and then :. The rest of
the function is a code block and is indented:

def <FUNCTION NAME>(<PARAMETERS>):
    <CODE BLOCK>

Simple explan -> A function is a block of code that performs a specific task whenever it is called. In bigger programs, where we have large amounts of code, it is advisable to
create or use existing functions that make the program flow organized and neat.

There are two types of functions:
1. Built in Functions
2. User defined Functions

Built-in functions:
These functions are defined and pre-coded in python. some examples of built in functions are as follows

min(), max(), len(), sum(), type(), range(), dict(), list(), tuple(), set(), print() etc

User defined functions:
We can create functions to perform specific task as per our needs. such functions are called user-defined functions

'''


def calculateGemotricMean(a,b):
    mean = (a*b)/(a+b)
    print(mean)

calculateGemotricMean(7,7)


def greaterNumber(a,b):
    if a > b:
        print("a is greater",a)
    elif b>a:
        print("b is greater",b)
    else:
        print("number is same")
greaterNumber(1,1)


def positioned(first,second):
    print(f"First: {first}")
    print(f"Second: {second}")

positioned(str("ashutosh"),str("pandey"))
positioned(1,2)

#With keyword arguments, assign each argument a default value:
def keywords(first=1,second=2):
    '''Default value is assigned'''
    print(f"First value:{first}")
    print(f"second value:{second}")

keywords()
keywords(0)
keywords(second='one',first='second')


'''
When using keyword parameters, all parameters defined after a keyword parameter
must be keyword parameters as well. All functions return a value. The return key‐
word is used to set this value. If not set from a function definition, the function
returns None:
'''

def no_return():
    '''no returned defined'''
    pass

result=no_return()
print(result)  #None print

def return_One():
    '''return 1'''
    return 1
return_One()
result = return_One()
print(result)


def average(a,b):
    print("The average is ", (a+b)/2)
average(4,6)
'''
Arguments in functions and return statements
1. Default Arguments
2. Keyword Arguments
3. Variable length Arguments
4. Required Arguments


'''
#1- Default arguments provide a default value while creating a functions. This way the functions assumes a default value even if a value is not provided in the functions call for that argument 

def name(fname, mname = 'parasar', lname='pandey'):
    print("Hello,", fname, mname, lname)

name("Ashutosh")

def average(a=9,b=1):
    print("The average is ", (a+b)/2)

average(4,5)  #--> this priority first if given 


#2- Keyword Arguments with key = value, this way the interpreter recognizes the arguments by the parameter name. Hence the order in which the arguments are passed does not matter.

def name(fname,mname,lname):
    print("hello,",fname,mname,lname)

name(fname="mark",mname="modi",lname="yo")

def average(a=9,b=1):
    print("The average is ", (a+b)/2)

average(a=5,b=5)


#3- required arguments is case where we don't pass the arguments with a key = value, syntax, then it is necessary to pass the arguments in the correct positional order and the number or arguments passed should match with
#actual function definition

def name(fname,mname,lname):
    print("hello,",fname,mname,lname)

name(fname="mark",mname="modi",lname="yo")  #needed arguments

def average(a,b=1):
    print("The average is ", (a+b)/2)

average(a=1,b=5)


#4- variable length argument --> sometimes we may need to pass more arguments than those defined in the actual functions. This can be done using variable length arguments
#1 way -> Arbitrary Arguments:  While creating a function, pass a* before the parameter name while defining the function. The function accessess the arguments by processing them in the form of tuple.

def name(*name):
    print("Hello", name[0],name[1],name[2])

name("Ashu","Pandey","Yo")


def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
    print("Average is: ", sum / len(numbers))

average(5,6,7,1,2,5,8)

print(19/4)


#2 Way -> keyword Arbitrary Arguments: while creating a function, pass a ** before the parameter name while defining the function. The function accessess the arguments by processing them in the form of dictionary.
def name(**name):
    print(type(name))
    print("Hello,", name["fname"], name['mname'],name["lname"])

name(mname="parasar", lname="pandey",fname="Ashutosh")



#Return statement is used to return the value of the expression back to the calling function.

def average(*numbers):
    print(type(numbers))
    sum = 0
    for i in numbers:
        sum = sum+i
#    return 7                    #priority first
    return sum / len(numbers)

c=average(5,6,7,1,2,5,8)
print(c)

    






    