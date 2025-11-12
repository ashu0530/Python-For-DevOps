#split function ARN number to print username

arn = "arn:aws:iam::123456789012:user/JohnDoe"

username = arn.split('/')[1]
print(username)  # Output: JohnDoe


name = "ashutosh"
print(name.upper())  # Output: ASHUTOSH

#add two kind of strings

str1 = "Hello"
str2 = "World"

result = str1 + str2    #concatenation of two strings
print(result)  # Output: HelloWorld

#print length of string
arn = "arn:aws:iam::123456789012:user/JohnDoe"
length = len(arn)
print(length)  # Output: 38

#stripping the whitespace
text = "   Hello, World!   "
stripped_text = text.strip()
print(stripped_text)  # Output: "Hello, World!"


#replace function
original_string = "Hello, World!"
modified_string = original_string.replace("World", "Python")
print(modified_string)  # Output: Hello, Python!

#stripping specific characters
text = "###Hello, World!###"
stripped_text = text.strip("#")
print(stripped_text)  # Output: "Hello, World!"

#split function
csv_string = "apple,banana,cherry"
fruits = csv_string.split(",")
print(fruits)  # Output: ['apple', 'banana', 'cherry']
print(fruits[1])  # Output: banana

#find function
text = "Hello, World!"
index = text.find("World")
print(index)  # Output: 7

#join function
words = ["Hello", "World", "from", "Python"]
sentence = " ".join(words)
print(sentence)  # Output: Hello World from Python

#lower function
name = "ASHUTOSH"
print(name.lower())  # Output: ashutosh

#count function
text = "hello world"
count = text.count("o")
print(count)  # Output: 2

#startswith function
text = "Hello, World!"
starts_with_hello = text.startswith("Hello")
print(starts_with_hello)  # Output: True

#endswith function
text = "Hello, World!"
ends_with_exclamation = text.endswith("!")
print(ends_with_exclamation)  # Output: True

#format function
name = "Ashutosh"      
age = 30
formatted_string = "My name is {} and I am {} years old.".format(name, age)
print(formatted_string)  # Output: My name is Ashutosh and I am 30 years old.

#f-string
name = "Ashutosh"   
age = 30
formatted_string = f"My name is {name} and I am {age} years old."
print(formatted_string)  # Output: My name is Ashutosh and I am 30 years old.

#escape characters
text = "He said, \"Hello, World!\""     
print(text)  # Output: He said, "Hello, World!"
path = "C:\\Users\\Ashutosh\\Documents\\file.txt"
print(path)  # Output: C:\Users\Ashutosh\Documents\file.txt

#multiline string
multiline_text = """This is line one.
This is line two.
This is line three."""
print(multiline_text)
# Output:
# This is line one. 
# This is line two.
# This is line three.

#raw string
raw_string = r"C:\Users\Ashutosh\Documents\file.txt"
print(raw_string)  # Output: C:\Users\Ashutosh\Documents\file.txt
path = r"C:\Users\Ashutosh\Documents\file.txt"
print(path)  # Output: C:\Users\Ashutosh\Documents\file.txt

#string slicing
text = "Hello, World!"
substring = text[7:12]
print(substring)  # Output: World
#negative indexing
text = "Hello, World!"
last_character = text[-1]
print(last_character)  # Output: !
sub_string = text[-6:-1]
print(sub_string)  # Output: World

#string immutability
text = "Hello, World!"
# text[0] = "h"  # This will raise a TypeError
modified_text = "h" + text[1:]
print(modified_text)  # Output: hello, World!

#string concatenation with +
str1 = "Hello"
str2 = "World"
result = str1 + " " + str2
print(result)  # Output: Hello World

#string repetition with *
text = "Hello! "
repeated_text = text * 3
print(repeated_text)  # Output: Hello! Hello! Hello!

#string membership with in
text = "Hello, World!"
contains_hello = "Hello" in text
print(contains_hello)  # Output: True

#string comparison
str1 = "apple"
str2 = "banana"
is_equal = str1 == str2
print(is_equal)  # Output: False
is_greater = str1 > str2
print(is_greater)  # Output: False

#string methods chaining
text = "   Hello, World!   "
modified_text = text.strip().upper().replace("WORLD", "PYTHON")
print(modified_text)  # Output: HELLO, PYTHON!

#string formatting with %
name = "Ashutosh"
age = 30
formatted_string = "My name is %s and I am %d years old." % (name, age)
print(formatted_string)  # Output: My name is Ashutosh and I am 30 years old.


#string alignment
text = "Hello"
left_aligned = text.ljust(20, '-')
print(left_aligned)  # Output: Hello---------------
right_aligned = text.rjust(20, '-')
print(right_aligned)  # Output: ---------------Hello
center_aligned = text.center(20, '-')
print(center_aligned)  # Output: -------Hello--------

#string partitioning
text = "username:password:email"
partitioned_text = text.partition(":")
print(partitioned_text)  # Output: ('username', ':', 'password:email')

#string zfill
number = "42"
padded_number = number.zfill(5)
print(padded_number)  # Output: 00042

#string encode and decode
text = "Hello, World!"
encoded_text = text.encode("utf-8")
print(encoded_text)  # Output: b'Hello, World!'
decoded_text = encoded_text.decode("utf-8")
print(decoded_text)  # Output: Hello, World!

#string translate
text = "Hello, World!"
translation_table = str.maketrans("Helo", "Jxxy")
translated_text = text.translate(translation_table)
print(translated_text)  # Output: Jxxxy, Wxrxd!

#adding numbers
num1 = "10"
num2 = "20"
sum_result = int(num1) + int(num2)
print(sum_result)  # Output: 30

num1 = 1
num2 = 2
sum_result = str(num1) + str(num2)
print(sum_result)  # Output: 12

#adding integers
num1 = 10
num2 = 20
sum_result = num1 + num2
print(sum_result)  # Output: 30

#adding float
num1 = 10.5
num2 = 20.3
sum_result = num1 + num2
print(sum_result)  # Output: 30.8

#adding integer and float
num1 = 10
num2 = 20.5
sum_result = num1 + num2
print(sum_result)  # Output: 30.5

#subtracting numbers
num1 = 20
num2 = 10
diff_result = num1 - num2
print(diff_result)  # Output: 10

#multiplying numbers
num1 = 5
num2 = 4
prod_result = num1 * num2
print(prod_result)  # Output: 20

#dividing numbers
num1 = 20
num2 = 4
div_result = num1 / num2
print(div_result)  # Output: 5.0
#floor division
floor_div_result = num1 // num2 
print(floor_div_result)  # Output: 5

#modulus
mod_result = num1 % num2
print(mod_result)  # Output: 0

#exponentiation
exp_result = num1 ** 2
print(exp_result)  # Output: 400

#type conversion
num_str = "100"
num_int = int(num_str)
print(num_int)  # Output: 100
num_float = float(num_str)
print(num_float)  # Output: 100.0

num_int = 50
num_str = str(num_int)
print(num_str)  # Output: "50"


#absolute value
num = -10
abs_value = abs(num)
print(abs_value)  # Output: 10

#rounding numbers
num = 10.5678
rounded_num = round(num, 2)
print(rounded_num)  # Output: 10.57

#maximum and minimum
num1 = 10
num2 = 20
max_value = max(num1, num2)
print(max_value)  # Output: 20

min_value = min(num1, num2)
print(min_value)  # Output: 10

#power function
power_value = pow(num1, 2)
print(power_value)  # Output: 100

#sum function
numbers = [1, 2, 3, 4, 5]
total_sum = sum(numbers)
print(total_sum)  # Output: 15
#length of number when converted to string
num = 12345
length = len(str(num))
print(length)  # Output: 5

#maximum digit in number
num = 573829
max_digit = max(str(num))
print(max_digit)  # Output: 9

#minimum digit in number
num = 573829
min_digit = min(str(num))
print(min_digit)  # Output: 2

#convert string to list of characters
text = "Hello"
char_list = list(text)
print(char_list)  # Output: ['H', 'e', 'l', 'l', 'o']




#Typecasting 
'''
The conversion one data type into other data tyoes is known as type casting in python
Support --> str(), hex(), 
Explict and Implict type casting
Explict programmer doing conversion while implict python intepreter doing itself

'''
a = "1"
b = "2"
print(a+b)
print(int(a)+int(b))
print(type(a))

#Implict type casting
c = 1.9
d = 9
#int + float = float
print(c+d)