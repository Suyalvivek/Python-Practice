if True:
    print('Conditional was True')
else:
    print('Conditional was false')

lang='Python'
if lang=='Python':
    print('Language is Python')
else:
    print('Language is not Python')

lang=''
if lang=='Python':
    print('Language is Python')
elif lang=='Java':
    print('Language is Java')

else:
    print('Language is not Python or Java')

''' comparison operators
==
!=
>
>=
<
<=
is
'''
'''
LOGICAL OPERATORS
and
or 
not
'''
user="admin"
is_loggedin =False
if(user=='admin' and is_loggedin):
    print('Admin Page')
else:
    print('Login Page')

if(user=='admin' or is_loggedin):
    print('Admin Page')
else:
    print('Login Page')

if(not is_loggedin):
    print('Login Page')
else:
    print('Welcome Page')

# is
a=[1,2,3]
b=[1,2,3]
print(a==b)
print(a is b)
print(id(a))
print(id(b))

a = [4,5,6]
b=a
print(a==b)
print(a is b)
print(id(a))
print(id(b))

# FALSE VALUES IN PYTHON
# False
# None
# ZERO OF ANY NUMERIC TYPE
# ANY EMPTY SEQUENCE [],'',()
# ANY EMPTY MAPPING {}
