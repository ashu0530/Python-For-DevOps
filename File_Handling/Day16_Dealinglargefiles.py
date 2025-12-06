'''
Docstring for File_Handling.Day16_Dealinglargefiles

Dealing with Large Files
 There are times that you need to process very large files. If the files contain data that
 can be processed one line at a time, the task is easy with Python. Rather than loading
 the whole file into memory as you have done up until now, you can read one line at a
 time, process the line, and then move to the next. The lines are removed from mem
ory automatically by Python’s garbage collector, freeing up memory.
 Python automatically allocates and frees memory. Garbage collec
tion is one means of doing this. The Python garbage collector can
 be controlled using the gc package, though this is rarely needed.

'''
import re
sourcePath = r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\bigdatafile.txt'
destPath = r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\bigdatadest.txt'
with open(sourcePath,'r') as sourcefile:
    with open(destPath, 'w' ) as destfile:
        for line in sourcefile:
            destfile.write(line)


'''
Notice that you can nest the with statements to open two files at once and loop
 through the source file object one line at a time. You can define a generator function
 to handle this, especially if you need to parse multiple files a single line at a time

'''

def line_reader(sourcePath):
    with open(sourcePath,'r') as sourcefile:
        for line in sourcefile:
            yield line



reader = line_reader(sourcePath)
print(reader,type(reader))  #generator

with open(destPath,'w') as destfile:
    for line in reader:
        destfile.write(line)




def processed_data(chunk):
    print(f"Read chunk size: {len(chunk)} bytes")
    with open(r'c:/Users/GFVM4731/Downloads/python-for-devops/File_Handling/pic.png','rb') as srcfile:
        while True:
            chunk = srcfile.read(1024)
            if chunk:
                processed_data(chunk)
            else:
                break

