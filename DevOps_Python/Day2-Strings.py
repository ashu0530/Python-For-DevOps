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



stringformatlog="%s + %s = %s" % (1,2,"Three") 
print(stringformatlog)
print(type(stringformatlog))

#control the number of places a float, %f, prints
floatprint="%.5f" % 1.234567
print(floatprint)
print(type(floatprint))


#String with placeholders {} These act as “slots” that will be filled later.
'''.format() method

The .format() method replaces those {} placeholders with the values you provide in order. '''

a='{} comes before {}'.format('first','second')
print(a)


'''You can specify index numbers in the brackets to insert values in an order different
 than that in the argument list.'''

a='{1} comes after {0}, but comes before {2}'.format('first','second','third')
print(a)

'''An even more powerful feature is that the insert values can be specified by name:
'''

a = '{firstname} with last name {lastname}'.format(firstname='ashutosh',lastname='pandey')
print(a)


# Here a dict works to supply the key values for name-based replacement fields
values = {'first': 'Bill', 'last': 'bailey'}
print("Won't you come home {first} {last}?".format(**values))

'''Format specifications are done using the format specification mini-language. Our
 topic also uses another type of language called f-strings.


 Python f-strings use the same formatting language as the format method, but offer a
 more straightforward and intuitive mechanism for using them. f-strings are prepen
ded with either f or F before the first quotation mark. Like the format string previ
ously described, f-strings use curly braces to demarcate replacement fields. In an f
string, however, the content of the replacement field is an expression. This approach
 means it can refer to variables defined in the current scope or involve calculations:
'''

a = 1
b = 2
ans = f"a is {a}, b is {b}. adding them result will be {a+b}"
print(ans)


count = 43
ans = f"|{count:5d}"
print(ans)

'''
Perfect — let’s break this one down carefully 👇

```python
count = 43
ans = f"|{count:5d}"
print(ans)
```

---

### 🔹 Step 1: `f"..."` — f-string

The `f` before the string means **formatted string literal** (f-string), introduced in Python 3.6.
It allows you to directly insert variables or expressions inside `{}`.

So here, `count` (which is `43`) is placed inside `{}`.

---

### 🔹 Step 2: Format specifier `:5d`

Inside `{count:5d}` →

* `:` introduces a **format specification**.
* `5` → means the **total width** of the output field should be **5 characters wide**.
* `d` → means **decimal integer** (used for numbers).

So `:5d` means:

> Print this integer right-aligned in a field that’s 5 characters wide.

---

### 🔹 Step 3: Evaluate the f-string

`count = 43` has **2 digits**,
but the width requested is **5**,
so Python adds **3 spaces to the left** to make it 5 characters total.

Hence:

```
'   43'
```

---

### 🔹 Step 4: The `|` before it

The `|` at the start is just a **visual marker** so you can see the padding.

When printed:

```text
|   43
```

You can clearly see there are 3 spaces between `|` and `43`.

---

✅ **Final Output**

```
|   43
```

---

### 💡 Tip:

You can left-align instead by using `<`:

```python
f"|{count:<5d}"
# Output: |43   
```

👉 Now the number is on the left, with padding on the right.


'''
from string import Template
greeting = Template("$hello Ashutosh")
print(greeting.substitute(hello="Hallo"))
#Hallo Ashutosh

print(greeting.substitute(hello="Zdravstvuyte"))
# 'Zdravstvuyte Ashutosh'

print(greeting.substitute(hello="Nǐn hǎo"))
# 'Nǐn hǎo Ashutosh'

