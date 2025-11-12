str()
my_list = list()
str(my_list)
print(my_list)


#Multiline string
multiline = '''This is a 
multiline string
which includes line breaks'''

print(multiline)



''' Remove some spaces whitespaces for example e. If some‐
one types " yes " in a form instead of “yes” you usually want to treat them the same.
Python strings have a strip method just for this case. It returns a string with the
whitespace removed from the beginning and end. There are also methods to remove
the whitespace from only the right or left side of the string:'''

input = "   I want more   "
print(input)
ans = input.strip()  #Removed the whitespace
print(ans)

ans2 = input.lstrip()
print(ans2)

ans3 = input.rstrip()
print(ans3)

'''Padding in your string you can use the ljust or
rjust methods. Either one pads with whitespace by default, or takes a character
argument: '''

output = "ashutosh"
ans = output.ljust(10)
print(ans)
ans2 = output.rjust(10,'*')
print(ans2)


'''
Sometimes you want to break a string up into a list of substrings. Perhaps you have a
sentence you want to turn into a list of words, or a string of words separated by com‐
mas. The split method breaks a string into a list of strings. By default, it uses white‐
space as the token to make the breaks. An optional argument can be used to add in
another character where the split can break:

'''

text = "Hello my name is ashutosh"
ans = text.split()
print(ans)
url = "gt.motomomo.io/v2/api/asset/143"
ans = url.split('/')
print(ans)
#['Hello', 'my', 'name', 'is', 'ashutosh']
#['gt.motomomo.io', 'v2', 'api', 'asset', '143']


'''
create a new string from a sequence of strings and join them into a
single string. This method inserts a string as a separator between a list of other
strings:

'''
items = ['cow','cat','human','bread']
ans = " and ".join(items)
print(ans)
#cow and cat and human and bread


name = "ashutosh pandey"
ans = name.capitalize()
ans2 = name.upper()
ans3 = name.title()
ans4 = name.swapcase()
print(ans,ans2,ans3,ans4)

'''
Python also provides methods to understand a string’s content. Whether it’s checking
the case of the text, or seeing if it represents a number, there are quite a few built-in
methods for interrogation. Here are just a few of the most commonly used methods:

'''
print("ashutosh".startswith('a'))   #True
print("ashutosh".startswith('b'))   #False
print('ashutosh'.endswith('osh')) #True
print('ashutosh123'.isalnum()) #True
print('ashutosh123'.isalpha()) #False
print('abc123'.isalnum())  #True

