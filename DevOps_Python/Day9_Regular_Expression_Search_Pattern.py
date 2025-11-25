'''
The need to match patterns in strings comes up again and again. You could be look
ing for an identifier in a log file or checking user input for keywords or a myriad of 
 other cases. You have already seen simple pattern matching using the in operation for
 sequences, or the string .endswith and .startswith methods. To do more sophisti
cated matching, you need a more powerful tool. Regular expressions, often referred
 to as regex, are the answer. Regular expressions use a string of characters to define
search patterns. The Python re package offers regular expression operations similar
 to those found in Perl. The re module uses backslashes (\) to delineate special charac
ters used in matching. To avoid confusion with regular string escape sequences, raw
 strings are recommended when defining regular expression patterns. Raw strings are
 prepended with an r before the first quotation mark.  '''

#Python strings have several escape sequences. Among the most
# common are line-feed \n and tab \t.

cc_list = '''Ezra Koenig <ekoenig@vpwk.com>,
...: Rostam Batmanglij <rostam@vpwk.com>,
   ...: Chris Tomson <ctomson@vpwk.com,
   ...: Bobbi Baio <bbaio@vpwk.com'''

print('Rostam' in cc_list)

import re
print(re.search(r'rostam', cc_list))

if re.search(r'Bobbi',cc_list):
    print("Found bobbi")

#What if you don't know exact name like it can be Bobbi or Robby or Bobby then?
'''
With regular expressions, you can use groups of characters, any one of which could
 appear in a spot. These are called character sets. The characters from which a match
 should be chosen are enclosed by square brackets in the regular expression definition.
 You can match on B or R, followed by obb, and either i or y:
'''

print( re.search('[RB]obb[yi]',cc_list))

'''
You can put comma-separated individual characters in a character set or use ranges.
 The range A–Z includes all the capitalized letters; the range 0–9 includes the digits
 from zero to nine:
'''
print(re.search(r'Chr[a-z][a-z]', cc_list))
print(re.search(r'tom[a-z][a-z]',cc_list))


'''
 The + after an item in a regular expression matches one or more of that item. A num
ber in brackets matches an exact number of characters
'''


'''
The + after an item in a regular expression matches one or more of that item. A num
ber in brackets matches an exact number of characters:
'''

print(re.search(r'[A-Za-z]+', cc_list))
print(re.search(r'[A-Za-z]{9}',cc_list))    #search 9 atleast character

'''
We can construct a match using a combination of character sets and other characters
 to make a naive match of an email address. The . character has a special meaning. It is
 a wildcard and matches any character. To match against the actual . character, you
 must escape it using a backslash:
'''

print(type(cc_list))

print(re.search(r'[A-Za-z]+@[a-z]+\.[a-z]+',cc_list)) #for email id catch in string

#Character classes
'''
 In addition to character sets, Python’s re offers character classes. These are premade
 character sets. 
 
1 -  Some commonly used ones are \w, which is equivalent to [a-zA
Z0-9_] 

2- \d, which is equivalent to [0-9]. You can use the + modifier to match for
 multiple characters:
'''

print(re.search(r'\w+',cc_list))

string="Aashutosh@gmail.com"
print(re.search('\w',string))
print(re.search('\w+',string))
print(re.search('\w+\@',string))
print(re.search(r'\w+\@\w+\.\w+',string))  #email fetch #raw string
print(re.search('\w+\@\w+\.\w+',string))

#here '\w fetch first character under [A-Za-z] like example Ashutosh --> print A
#here \w+ fetch all charcter [A-Za-z] like Aashutosh --> print Aashutosh
#here \w+\@   in last find any string having @ with it



#groups
'''
Groups
 You can use parentheses to define groups in a match. These groups can be accessed
 from the match object. They are numbered in the order they appear, with the zero
 group being the full match:
'''

print(re.search(r'(\w+)\@(\w+)\.(\w+)',string))
match = re.search(r'(\w+)\@(\w+)\.(\w+)',string)
print(match[0])
print(match[1])
print(match[2])



'''
Named Groups
You can also supply names for the groups by adding ?P<NAME> in the group defini
tion. Then you can access the groups by name instead of number:
'''

matched = re.search(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)',string)
print(matched.group('name'))
print(matched.group('SLD'))
print(matched.group('TLD'))

print(f"Here is the name {matched.group('name')} and a Secondary level doman is {matched.group('SLD')} and a top level domain is {matched.group("TLD")}")



'''
Find All
Up until now, we have demonstrated returning just the first match found. We can also
use findall to return all of the matches as a list of strings:
'''

matched = re.findall(r'\w+\@\w+\.\w+',cc_list)
print(type(matched))
print(matched)

matched = re.findall(r'(\w+)\@(\w+)\.(\w+)',cc_list)
print(matched[0])

names = [x[0] for x in matched]
print(names)

for i in matched:
    print(f" name of all id found is {i[0]}")



'''
Find Iterator
 When dealing with large texts, such as logs, it is useful to not process the text all at
 once. You can produce an iterator object using the finditer method. This object pro
cesses text until it finds a match and then stops. Passing it to the next function
 returns the current match and continues processing until finding the next match. In
 this way, you can deal with each match individually without devoting resources to
 process all of the input at once:
'''

matched = re.finditer(r'\w+\@\w+\.\w+',cc_list)
print(next(matched).group())
print(next(matched).group())
print(next(matched).group())
print(next(matched).group()) #iteration till 3 index


matched = re.finditer(r'(?P<name>\w+)\@(?P<SLD>\w+)\.(?P<TLD>\w+)',cc_list)

for i in matched:
    print(i.groupdict())

'''
{'name': 'ekoenig', 'SLD': 'vpwk', 'TLD': 'com'}
{'name': 'rostam', 'SLD': 'vpwk', 'TLD': 'com'}
{'name': 'ctomson', 'SLD': 'vpwk', 'TLD': 'com'}
{'name': 'bbaio', 'SLD': 'vpwk', 'TLD': 'com'}
'''

