'''
Docstring for File_Handling.Day11_Automating_file_and_filesystem

 Reading and Writing Files
 You can use the open function to create a file object that can read and write files. It
 takes two arguments, the path of the file and the mode (mode optionally defaults to
 reading). You use the mode to indicate, among other things, if you want to read or
 write a file and if it is text or binary data. You can open a text file using the mode r to
 read its contents. The file object has a read method that returns the contents of the
 file as a string:

'''
import re

file_path=r"c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\cloudtrail.log"
open_file=open(file_path,'r')
text = open_file.read()
#print(text)
print(type(text),len(text))

print(text[56])
print(open_file)
print(text[0])


'''It is a good practice to close a file when you finish with it. Python
 closes a file when it is out of scope, but until then the file consumes
 resources and may prevent other processes from opening it.'''
open_file.close() 


'''You can also read a file using the readlines method. This method reads the file and
 splits its contents on newline characters. It returns a list of strings. Each string is one
 line of the original text:'''

open_file=open(file_path,'r')
text = open_file.readlines()
print(type(text),len(text))
print(text[0])



'''
A handy way of opening files is to use with statements. You do not need to close a file
explicitly in this case. Python closes it and releases the file resource at the end of the
 indented block:
'''
with open(file_path,'r') as open_file:
    text = open_file.readlines()
    print(text)
print(open_file.closed)


#Read file as binary 
file_path = r"c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\pic.png"
with open(file_path,'rb') as file:
    text = file.readlines()
print(text,len(text),type(text))
print(text[0])

'''
To write to a file, use the write mode, represented as the argument w. The tool direnv
 is used to automatically set up some development environments. You can define envi
ronment variables and application runtimes in a file named .envrc; direnv uses it to
 set these things up when you enter the directory with the file. You can set the envi
ronment variable STAGE to PROD and TABLE_ID to token-storage-1234 in such a file
 in Python by using open with the write flag:
'''


###WARNING  Be warned that pathlib’s write method will overwrite a file if it already exists.
text = '''export STAGE=PROD
...: export TABLE_ID=token storage-1234'''

with open('.envrc','w') as opened_file:
    opened_file.write(text)


prod = "clr-flip-prod-namespace name"
newnsname="sugar-namespace"
with open('prod.txt','w') as writefile:
    writefile.write(prod)
    writefile.write(newnsname)

'''
The open function creates a file if it does not already exist and overwrites if it does. If
you want to keep existing contents and only append the file, use the append flag a.
'''
#append
text1= 'abcd'
with open('text1','a') as text:
    text.write(text1)

'''If
 you are writing nontext content, such as the contents of a .jpeg file, you are likely to
 corrupt it if you use either the w or a flag. This corruption is likely as Python converts
 line endings to platform-specific ones when it writes text data. To write binary data,
 you can safely use wb or ab.'''


'''
Two useful features of pathlib are convenience functions for
 reading and writing files. pathlib handles the file object behind the scenes. The fol
lowing allows you to read text from a file:
'''
import pathlib
path = pathlib.Path(r"c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\cloudtraillogreader.py")
path2 = pathlib.Path(r"c:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\pic.png")
# To read binary data, use the path.read_bytes method
print(path.read_text(),path2.read_bytes())


'''
When you want to overwrite a file or write a new file, there are methods for writing
 text and for writing binary data:
'''
path = pathlib.Path("application.config")
path.write_text("LOG:DEBUG")