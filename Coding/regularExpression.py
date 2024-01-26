from re import *

string = "Hello, World"

# find all function
x = findall('o', string)
print(x)

# search function
x = search('o', string)
print(x.span())

# split function
x = split('o', string)
print(x)

# sub function
x = sub('o', "*", string)
print(x)