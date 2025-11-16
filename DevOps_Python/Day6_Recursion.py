'''
Recursion in python
Recursion is the process of defining something in terms of itself.

Python Recursive Function
In Python, we know that a function can call other functions. It is even possible for the function to call itself. These types of construct are termed as recursive functions.
'''

# factorial(7) = 7*6*5*4*3*2*1
# factorial(6) = 6*5*4*3*2*1
# factorial(5) = 5*4*3*2*1
# factorial(4) = 4*3*2*1
# factorial(0) = 1

# factorial(n) = n * factorial(n-1)

def factorial (n):
    if n == 0 or n == 1:
        return 1
    else:
        return n* factorial(n-1)



print(factorial(3))
print(factorial(5))

'''
working need print(factorial(5))
n* factorial(n-1) where n = 5
5* factorial(4)
5*4 factorial(3)
5*4*3 factorial(2))
5*4*3*2 (factorial(1))
if condition triggered 
5*4*3*2*1 

'''

#Fibonacci Sequence

def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1 or n == 2:
        return 1
    else:
       return fibonacci(n-1) + fibonacci ( n-2)

print(fibonacci(10))
