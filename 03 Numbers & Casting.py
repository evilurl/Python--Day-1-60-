#######################
#       NUMBERS       #
#######################
# There are 3 numeric types in Python
# 1. int
# 2. float
# 3. complex

# let
x = 1 # int
y = 10.5 # float
z = 29j # complex

# now we'll check their types
print(type(x))
print(type(y))
print(type(z))

print('\n')

#----< INT >----
# int is a whole number, positive or negative which don't have decimals in it.

print('INTEGER')
x = 1
y = 199999
z = -39

# now we'll check their types
print(type(x))
print(type(y))
print(type(z))

print('\n')

#----< FLOAT >----
# float is a whole number, positive or negative which have decimals in it. It can have one or more decimals in it.
# floats can also be scientific numbers with an 'e'/'E' to indicate the power of 10.

print('FLOAT')
x = 1.01
y = 1.0001
z = -399.99

# now we'll check their types
print(type(x))
print(type(y))
print(type(z))

print('\n')

#----< COMPLEX >----
# Complex numbers are imaginary numbers written with 'j' as an imaginary part.

print('COMPLEX')
x = 1j
y = 22.2j
z = -3j

# now we'll check their types
print(type(x))
print(type(y))
print(type(z))

print('\n')

#----< CONVERSION >----
# Note: float, int --> int, float, complex
# but complex can't convert into int, float

x = 22 # int
a = float(x)
print(type(a), x)

y = 22.01
b = int(y)
print(type(b), y)

z = 11
c = complex(z)
print(type(c), z, c)

print('\n')

#######################
#       CASTING       #
#######################

# Casting is specifying the data type of an existing variable or a new variable. 

# By default when a variable is declared then its data type is automatically declared by compiler e.g; x = 5 ; then it'll be automatically declared as an INT. But we can change it's data type.

# let
x = 5 # int
print('Before casting', type(x))
print('After casting', type(float(x)))

print('\n')

#----< INT >----
x = int(1)
y = int(2.55)
z = int('33')

print(type(x), x)
print(type(y), y)
print(type(z), z)

print('\n')

#----< FLOAT >----
w = float('4.5')
x = float(19.9)
y = float(2)
z = float('33')

print(type(w), w)
print(type(x), x)
print(type(y), y)
print(type(z), z)

print('\n')