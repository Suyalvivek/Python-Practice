message = "Hello World"
print(message)
print(len(message))
print(message[-11])
print(message[0:5])
print(message.lower())
print(message.upper())
print(message.count("Hello"))
print(message.find("Hello"))
print(message.replace("Hello","World"))

greeting =  'hello'
name = 'Vivek'
message = greeting + name
print(message)
message = f'{greeting} {name}'
print(message)
print(dir(message))
print(help(str))
print(help(str.lower))