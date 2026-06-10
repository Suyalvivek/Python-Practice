#STRINGS
# STRINGS ARE IMMUTABLE
from dict import student

name = "vivek suyal"
print(name)
print(type(name))
print(name.upper())
print(name.lower())
print(name.capitalize())
print(name.title())

# ACCESSING CHARACTERS OF A STRING
print(name[0])
print(name[3])
print(name[-1])
print('----------')
# USING RANGE [start:end:skip]
print(name[1:3])
print(name[1:])
print(name[:9])
print(name[::-1])

# USING LOOP TRAVERSAL
for ch in name:
    print(ch)
# SPLIT THE STRING
list = name.split()
print(list)
# Replace in string
new_str  = name.replace('suyal','sharma')
print(new_str)
#FIND AN INDEX
idx = name.find('suyal')
print(idx)

#COUNT A CHARACTER
count = name.count('v')
print(count)

#LENGTH OF A STRING
length = len(name)
print(length)
#FSTRINGS
print(f'hi {name}')

# CONCATENATE
f_name = 'yogi'
l_name = 'su '
full_name = (f_name+l_name)
print(full_name)

# REMOVE EXTRA SPACES
print(full_name.strip())

# JOINING THE STRING
list = ['vivek','chander','suyal']
joined_list = '_'.join(list)
print(joined_list)

# LISTS
# LISTS ARE ORDERED AND MUTABLE
fruits = ['Apple','Banana','Orange','Papaya']
print(fruits)
# LENGTH OF LIST
print(len(fruits))

#ACCESSING THE ELEMENTS OF LIST
#SIMILAR LIKE STRINGS
#INDEX WISE
print(fruits[0])
print(fruits[1])
print(fruits[2])
print(fruits[3])
# print(fruits[4])ERROR
# SLICE
print(fruits[0:2])

#FOR LOOP
for fruit in fruits:
    print(fruit)

# USING INDEX
for i in range(len(fruits)):
    print(i,fruits[i])
# MEMBERSHIP OPERATOR

print("Apple" in fruits)
print("Mango" in fruits)

# MUTABLE
print('Org List',fruits)
fruits[0] = 'Kiwi'
print('Mutated list',fruits)

# LIST OPN
#APPEND -> to insert at last of list
fruits.append('Anaar')
print('Appended list',fruits)

#INSERT -> TO insert element at any index
fruits.insert(0,'Melon')
print(fruits)

#REMOVE->removes by value
fruits.remove('Anaar')
print(fruits)

#POP-> REMOVES LAST ELEMENT
popped = fruits.pop()
print(popped)
print(fruits)
# DELETE BY INDEX
del(fruits[0])
print(fruits)
#CONCATENATION OF LIST
list1=[2,1]
list2=[3,4]
list3=list1+list2

print(list3)

# REPETITION
print([1,2,'Apple']*3)
# Counting a list element frequency
list = [1,2,3,4,1,3,3]
print(list.count(3))
# TO FIND INDEX
print(list.index(3))
# SORT
# WE USE list.sort() for in place sorting
# sorted() for returning a new list
list.sort()
print(list)
list.sort(reverse=True)
print(list)
print(list3)
list4=sorted(list3)
print(list4)
print(list3)
# REVERSE A LIST
list4.reverse()
print(list4)
# COPY A LIST
list5 = list4.copy()
print(list5)


#LIST COMPREHENSION
squares=[i*i for i in range(5)]
print(squares)
print(sum(squares))
print(min(squares))
print(max(squares))

# Tuples
# Tuples are like arrays but are immutable
info=('vivek',21,'B.Tech ECE')
print(info)
# info[0]='yogesh' CAN'T REASSIGN
# print(info)
t=()
print(type(t))
t=(5)
print(type(t))
t=(3,)
print(type(t))
tup1=(1,2,3,4)
num1,num2,num3,num4=tup1
print(num1)
print(num2)
# TUPLE CAN BE KEY OF A DICTIONARY
location={
    (22.3,28,7):"Delhi"
}
print(location)

# SETS
#UNORDERED
#UNIQUE VALUES
nums={1,2,11,2,11,13}
print(nums)
# CREATE AN EMPTY SET
nums={}
print(type(nums))
nums=set()
print(type(nums))
nums=[1,2,3,44,45,1,1,1]
set = set(nums)
print(set)
# TO ADD AN ELEMENT
# SINGLE ELEMENT
set2={10,30,40}
set2.add(90)
# MULTIPLE ELEMENTS
set2.update([90,40,20])
print(set2)
set2.remove(90)
print(set2)

# SET OPERATIONS
nums1={1,2,3,4,1,13}
nums2={1,3,5,6,2,5}
print(nums1.intersection(nums2))
print(nums1.union(nums2))
print(nums1.difference(nums2))
print(nums1.symmetric_difference(nums2))
print(nums1.issubset(nums2))

# DICTIONARY

info = {
    "name":"vivek",
    "age":21,
    "occupation":"none"
}
print(type(info))
print(info)
print(info["name"])
print(info["age"])

# IF NOT SURE THAT KEY EXISTS
# print(info["phone"])
print(info.get("phone"))
print(info.get("phone","Not exists"))

#ADD NEW KEY VALUE PAIR
info["phone"]="935768765787"
print(info)
#UPDATE VALUES
info["phone"]="79898789898"
# TO UPDATE MULTIPLE VALUES SIMULTANEOUSLY
info.update({
    "name":"vivek",
    "age":23,
})

print(info)
#DELETE
del info["name"]
print(info)
#POP
age = student.pop("age")
print(age)
print(info)
#KEY CAN  BE A STRING,NUM,TUPLE
print(info.keys())
print(info.values())

# TRAVERSE
for key in info:
    print(key)
for key in info.keys():
    print(key)
for value in info.values():
    print(value)

for key,value in info.items():
    print(key,value)

print(info.items())
print("phone" in info)
print("address" in info)

# NESTED
student={
    "name":"vivek",
    "address":{
        "street":"",
        "city":"",
        "state":"",
    }

}
#length
print(len(info))