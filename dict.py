student = {
    "name":"Vivek",
    "age":21,
    "courses":['Python','JS']
}
print(student)
print(student['name'])
print(student['age'])
print(student['courses'])
# print(student['notexists'])
print(student.get('notexists','Nahi hai'))
print(student.keys())
print(student.values())
print(student.items())
for key in student:
    print(key)

for value in student.values():
    print(value)
for key,value in student.items():
    print(key,value)
