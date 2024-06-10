#----< STRINGS >----
# """
# Strings in python are either surrounded by a single quotation mark or a double quotation mark. 
# """

#----< SLICING STRINGS >----
name  = "Harry James"
print(len(name)) # Prints the length of the string.

print(name[0]) # Prints the first letter in a string.
print(name[-1]) # Prints the last letter in a string.
print(name[0:3]) # Prints string from index 0 to index 3
print(name[0:]) # Prints completes string.
print(name[:3]) # Prints string upto index 3.
print(name[:]) # Prints complete string.
print(name[::-1]) # Prints the string in reverse manner.

print("\n")

#----< ESCAPE SEQUENCES >----

# such as:
#   \\ - backslash
#   \' - single quote
#   \" - inverted double quote
#   \n - new line
#   \r - carriage return
#   \t - tab
#   \b - backspace
#   \f - form feed
#   \ooo - octal value
#   \xhh - hex value

country = '\\Pakistan' #   \\ - backslash
print(country)

country = '\'Russia' #   \' - single quote
print(country)

country = '\"Mongolia' #   \" - inverted double quote
print(country)

country = '\nMonaco' #   \n - new line
print(country)

country = '\rTurkey' #   \r - carriage return
print(country)

country = '\tMali' #   \t - tab
print(country)

country = '\bMalaysia' #   \b - backspace 
print(country)

country = '\fQatar' #   \f - form feed
print(country)


country = '\110Iraq' #   \ooo - octal value
print(country)

country = '\x65Turkey' #   \xhh - hex value
print(country)

print("\n")

#----< Formatted Strings >----
first = 'Harry'
last = 'James'

fullName = first + ' ' + last
print(fullName)

fullName = f"{first} {last}"
print(fullName)

fullName = F"{first} {last}"
print(fullName)

print("\n")

#----< String Methods >----

course = 'Python101'
print(course.upper())

course = 'Python101'
print(course.lower())

course = 'python101 program'
print(course.title())

course = '  python101 program'
print(course)
print(course.strip()) # removes spaces in the start
print(course.lstrip()) # removes spaces from left
print(course.rstrip()) # removes spaces from the right
print(course.find('101')) # return index of the number to find
print('pro' in course) # return value in ture/false
print('hello' not in course)
print(course.replace('p' , 'h'))


