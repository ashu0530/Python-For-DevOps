'''You may find yourself dealing with data stored as comma-separated values (CSV).
 This format is common for spreadsheet data. You can use the Python csv module to
 read these easily:'''
import re
import csv
with open(r'C:\Users\GFVM4731\Downloads\python-for-devops\File_Handling\username.csv','r') as csvread:
    file = csv.reader(csvread,delimiter=",")
    for i in range(5):
        print(next(file))


'''
The csv reader object iterates through the .csv file one line at a time, allowing you to
 process the data one row at a time. Processing a file this way is especially useful for
 large .csv files that you do not want to read into memory all at once. Of course, if you
 need to do multiple row calculations across columns and the file is not overly large,
 you should load it all at once.

'''


'''
The Pandas package is a mainstay in the data science world. It includes a data struc
ture, the pandas.DataFrame, which acts like a data table, similar to a very powerful
 spreadsheet. If you have table-like data on which you want to do statistical analysis or
 that you want to manipulate by rows and columns, DataFrames is the tool for you. It
 is a third-party library, so you need to install it with pip. You can use a variety of
 methods to load data into the DataFrames; one of the most common is from a .csv
 file:
'''

import pandas as pd

file = pd.read_csv(r'c:/Users/GFVM4731/Downloads/python-for-devops/File_Handling/panda_datafile.csv')
print(type(file))

#You can take a look at the top rows of your DataFrame using the head method
print(file.head(3))

print(file.describe())

#you can view a single column of data by using its name in square brackets:
print(file['First Name'])