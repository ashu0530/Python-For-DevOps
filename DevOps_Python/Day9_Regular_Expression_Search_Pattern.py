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


'''
 The + after an item in a regular expression matches one or more of that item. A num
ber in brackets matches an exact number of characters
'''