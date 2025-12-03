import re
with open(r'C:\Users\GFVM4731\Downloads\python-for-devops\File_handling\iam.json','r') as open_file:
    text = open_file.readline()
    print(type(text))    #string
    text=open_file.readlines() 
    print(type(text)) #list
    print(text)

'''need to parse this string (or strings) into data structures and types
 that match the original, which may be a great deal of work. A far better way is to use
 the json module:'''

import json
with open(r'C:\Users\GFVM4731\Downloads\python-for-devops\File_handling\iam.json','r') as jsonfile:
    jsontext = json.load(jsonfile) #dictionary type
print(jsontext,type(jsontext))



'''
The pprint module automatically formats Python objects for
 printing. Its output is often more easily read and is a handy way of
 looking at nested data structures.
'''
from pprint import pprint
pprint(jsontext)

