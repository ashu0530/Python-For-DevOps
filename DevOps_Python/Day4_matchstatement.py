#Match statements present in v3.10 > 
'''
To implement switch-case like characterstics very similar to if-else functionalities, we use a match case in python it is similar like switch case statement like in c++,java
a match statement  will compare a given variable's value to different shapes also referred to as the pattern, the main idea is to keep on comparing the variable with all the present
patterns untill it fits into one.

The match statement consist of 3 main entities

1 - The match keyword.
2 - One or more case clauses.
3 - Expression for each case.

The case clause consists of a pattern to be matched to the variable, a condition to be evaulated if the pattern matches, and a set of statements to be executed if the pattern matches.

'''

x = int(input("Enter the value of x: "))
match x:
    case 0:
        print("X is zero")
    case 4:
        print("x is 4")

    case _ if x==90:
        print(x,"is  90")
    case _ if x!=80:
        print(x,"x is not 80")
    case _:                                 #if nothing match then print
        print(x)
