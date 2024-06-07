# Variables can store data of different types and different types can do differnt things.

# In Python we've:
    # 1. Numeric (int, float)
    # 2. Text/String (str)
    # 3. Boolean (bool(true/false))
    # 4. Sequence (list, tuple, range)
    # 5. Mapping (dict) 

# To check the data type of any data we use:
# type() and pass the value or variable name to get an output.
# For example; 
# x = 10 # it's an int type
# type(x) # it'll tell us that variable 'x' is an integer data-type

#--> int
a = 10 
print(type(a), a)

#--> float
b = 17.5
print(type(b), b)

#--> str
c = 'evilurl'
print(type(c), c)

#--> bool
d = True
print(type(d), d)

#--> list
e = [1, 2, 4, 6, 9]
print(type(e), e)

#--> tuple
f = ('hi' , 'privet' , 'hello')
print(type(f), f)

#--> rang
g = range(19)
print(type(g), g)

#--> dict
h = {1:'a' , 2:'b' , 'c':3 , 'd':4 , 'e':5}
print(type(h), h)

#----< SETTING A DATA-TYPE >----
i = int(10.5)
print(type(i), i)

j = float(13)
print(type(j), j)

k = int(True)
print(type(k), k)

l = float(False)
print(type(l), l)

m = i + j
print(type(int(m)), int(m))