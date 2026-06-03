courses = ['Math','Science','Engineering']
for course in courses:
    print(course)

for i in range(5):
    print(i)

for i in range(1,6):
    print(i)

for i in range(1,6):
    for s in "abc":
        print(i,s)

for i in range(1,5):
    if(i==3):
        print("found",i)
        break
    print(i)

for i in range(1,5):
    if(i==3):
        print("found",i)
        continue
    else:
        print(i)


x =0
while(x<5):
    print(x)
    x+=1

while(True):
    if(x==5):
        break
    print(x)
    x+=1
