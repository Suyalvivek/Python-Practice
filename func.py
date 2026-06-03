def new_func():
    print('Hello World.')


# DRY PRINCIPLE
new_func()
new_func()
new_func()
new_func()
new_func()

def greeting(name):
    print(f'Hello {name}')

greeting('Vivek')
greeting('Vikas')

def salutations(name,msg):
    return f'Hello {name}, {msg}'
res = salutations('Vivek','How are u doing?').upper()
print(res)
# DEFAULT PARAMETERS
def def_salutations(name,msg='how are u'):
    return f'Hello {name}, {msg}'
res = def_salutations('Vivek').upper()
print(res)

def student_info(*args,**kwargs):
    """ Args and Kwargs"""
    print(args)
    print(kwargs)
student_info('Maths','Science','History',name='Vivek',age=22)

