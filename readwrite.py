f = open('book.txt','r')
print(f.read())
f.close()
print(f.closed)

f = open('book.txt','w')
f.write("I love python")
f.close()

f = open('book.txt','a')
f.write(" I love javascript")
f.close()

# WITH STATEMENT (we need not to close by ourself)
with open('func.py','r') as f:
    print(f.read())
print(f.closed)