#!/usr/bin/python

# 00-datatypes

# Strings:
## trings are very powerful datatypes.
## you can sum strings like so
a = "hello i'm" + " a python string"
# "hello i'm a python string"

# String indexes
## Note that these are diferences from the slice indexes
## these are for the machinem they start by 0
a[0] # "h"
a[1] # "e"
a[2] # "l"
a[3] # "l"
a[4] # "o"

a[-1] # "g"
a[-2] # "n"
a[-3] # "i"
a[-4] # "r"
a[-5] # "t"
a[[-6] # "s"
## you can also slice strings
## is pretty similar to accesing list elements by index
## you just tell the string which indexes the limits will be
## the slice works like this:
# [start:end:step]
## it will crop the string from the 'start' index
## up to the 'stop' index.
## you can also asign the step paratemer
# Note: indexes must be in human form (starting from 1, not 0)
a[0:5:] # "hello"
a[6:] # "i'm a python string"
a[::2] # hloimapto tig"

## is weird that you can sum strings, but you can't 	substract them
try:
    "hello" - "o"
except SyntaxError:
    print "I told you so"
    
## Apart from adding strings you can multiply them
"hello " * 2
## 'hello hello '
## This sometimes is usefull for writing lines on the terminal :)
"#" * 80

## When replacing text, you can split the string into items
## Each item will be in the middle of the replacing word:

splited = a.split("python")
# ["hello i'm a ", " string"]
## and then you just can join it
"ruby".join(splited)
# "hello i'm a ruby string"

a.replace("python", "ruby") # Same result

# String manipulation
## you can force a string to be a title
a.title() # Uppercases the first letter in each word
## a lowercase string
a.lower() # lowercases each letter, usefull for string comparisson
## a upercase string
a.upper() # Upercases each letter, usefull for yelling =)

# String validation
a.islower() # True
a.isupper() # False
a.istitle() # False
a.title().istitle() # True
#
a.isalpha() # False
a[0].isalpha() # True
a[0].isalnum() # False
a[0].isdigit() # False
a[0].isspace() # False

a.strip() # Removes whistespaces from left and right side of the string
a.splitlines() # Same result as .split("\n")
