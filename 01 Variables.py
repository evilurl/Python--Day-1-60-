# Variables are containers for storing values
# Variables names are case sensitive
# 
x = 5 # int
y = 'evil' # string
z = 10.5 # float

print(x)
print(y)
print(z)
print('\n')
#----< CASTING >----
a = str(x)
b = int(z)

#----< TYPE >----
print('Previously type of x is: ',type(x))
print('Now type of x is: ',type(a))
print('Previously type of z is: ',type(z))
print('Now type of z is: ',type(b))
print('\n')
#----< Rules for Python variables >----
# 1. A variable name must start with a letter or the underscore character
# 2. A variable name cannot start with a number
# 3. A variable name can only contain alpha-numeric characters and underscores (A-z, 0-9, and _ )
# 4. Variable names are case-sensitive (age, Age and AGE are three different variables)
# 5. A variable name cannot be any of the Python keywords.

# Legal variable names are:
myvar = 'evil' 
my_var = 'evil'
_my_var = 'evil'
myVar = 'evil'
MYVAR = 'evil'
myvar2  = 'evil'

print(myvar)
print(my_var)
print(_my_var)
print(myVar)
print(MYVAR)
print(myvar2)
print('\n')
# Other:
myVariableName = 'evilurl' # Camel Case
MyVaribaleName = 'evilurl' # Pascal Case
my_variable_name = 'evilurl' # Snake Case

print(myVariableName)
print(MyVaribaleName)
print(my_variable_name)
print('\n')
#----< Many values to Multiple Variables >----
d, e, f = 'Hello', 'Hey', 'Hi'
print(d)
print(e)
print(f)
print('\n')
#----< One to Many Variables >----
g = h = i = 'blyat'
print(g)
print(h)
print(i)
print('\n')
#----< UnPack Collection >----
fruits = ['mango', 'orange', 'banana']
j, k, l = fruits
print(j)
print(k)
print(l)
print('\n')

print(j,k,l)
print(j + k + l)
print('\n')

#----< GLOBAL VARIABLES >----
x = 'awesome'
def myfun():
    print('it is' , x)

myfun()
print('it is ' + x)
print('\n')

#----< GLOBAL KEYWORD >----
def myfun2():
    global y
    y = 'blyat'
    print('you',y)

myfun2()
print('you ' + y)
print('\n')

