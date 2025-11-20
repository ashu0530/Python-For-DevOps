# Write a python program to translate a message into secret code language. Use the rules below to translate normal English into secret code language

# Coding:
# if the word contains atleast 3 characters, remove the first letter and append it at the end
#   now append three random characters at the starting and the end
# else:
#   simply reverse the string

# Decoding:
# if the word contains less than 3 characters, reverse it
# else:
#   remove 3 random characters from start and end. Now remove the last letter and append it to the beginning

# Your program should ask whether you want to code or decode

#harry =  rew arryh dsa

# string = "abcd"
# a = list(string)
# print(type(a))
# print(a)

# a = ['a','b','c','d']
# print(type(a))
# temp=a[0]
# a.pop(0)
# a.append(temp)
# print(a)

import random
import string


def encoder(userinput):
    randomlength=3
    a = list(userinput)
    if len(a) >= 3:
        temp=a[0]
        a.pop(0)
        a.append(temp)
    res = ''.join(a)
    random_string1 = ''.join(random.choices(string.ascii_lowercase,k=randomlength))
    random_string2 = ''.join(random.choices(string.ascii_lowercase,k=randomlength))
    print(random_string1+res+random_string2)

    
    
    
    



        





userinput = input("Enter your word: ")
encoder(userinput)

