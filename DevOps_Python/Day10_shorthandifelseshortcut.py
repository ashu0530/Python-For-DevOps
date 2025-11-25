'''
If ... Else in One Line
There is also a shorthand syntax for the if-else statement that can be used when the condition being tested is simple and the code blocks to be executed are short. Here's an example:
'''
a = 3306
b = 3303
print("A") if a>b else print("=") if a == b else (print("B"))


c = 9 if a>b else 0 
print(c)

#result = value_if_true if condition else value_if_false

'''
if condition:
    result = value_if_true
else:
    result = value_if_false



Conclusion
The shorthand syntax can be a convenient way to write simple if-else statements, especially when you want to assign a value to a variable based on a condition.
However, it's not suitable for more complex situations where you need to execute multiple statements or perform more complex logic. In those cases, 
it's best to use the full if-else syntax.


'''