'''
Docstring for File_Handling.Day16_Encryptiontopic

Encrypting Text
 There are many times you need to encrypt text to ensure security. In addition to
 Python’s built-in package hashlib, there is a widely used third-party package called
 cryptography. Let’s take a look at both.

Hashing with Hashlib
 To be secure, user passwords must be stored encrypted. A common way to handle
 this is to use a one-way function to encrypt the password into a bit string, which is
 very hard to reverse engineer. Functions that do this are called hash functions. In
 addition to obscuring passwords, hash functions ensure that documents sent over the
 web are unchanged during transmission. You run the hash function on the document
 and send the result along with the document. The recipient can then confirm that the
 value is the same when they hash the document. The hashlib includes secure algo
rithms for doing this, including SHA1, SHA224, SHA384, SHA512, and RSA’s MD5.
 This is how you would hash a password using the MD5 algorithm:

'''

import hashlib
secret = "This is the password of document is 123456"
bsecret = secret.encode()   #convert in bytes class bit string
print(bsecret,type(bsecret))

m = hashlib.md5(bsecret)
print(m.digest())

#2nd method
m = hashlib.md5()
print(m,type(m))

m.update(bsecret)
print(m.digest())  # Notice that if your password or document is a string, you need to turn it into a binary string by using the encode method.


