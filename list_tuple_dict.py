#LIST
empty_list_1 = []
empty_list_2=list()
language = ['Hindi','English','French','Spanish']
print(language)
print(len(language))
print(language[0])
print(language[2:])
print(language[:3])
language.append('Urdu')
print(language)
language.insert(0,'Sanskrit')
print(language)

language2=['Mandarin','German','Japanese']
# language.append(language2)
language.insert(0,language2)
print(language)

print(language.extend(language2))
print(language)


value = language.pop()
print(value)
print(language)
# language.remove('Urdu')
print(language)
#----------------------New List-------------------------
courses=['Maths','Science','Engineering','Technology']

print(courses)
courses.sort()
print(courses)
courses.reverse()
print(courses)

nums=[1,34,5,243,4,1234]
print(nums)
nums.sort(reverse=True)
print(nums)
nums.sort()
print(nums)

# get a new sorted list
new_nums = sorted(nums)
print(new_nums)
print(min(nums))
print(max(nums))
print(sum(nums))

# FIND INDEX OF ANY LIST ELEMENT
print(nums.index(1234))

# CHECK IF ELEMENT EXISTS IN LIST OR NOT
print(4 in nums)
print(6 in nums)

# TO PRINT EACH LIST ELEMENT
for num in nums:
    print(num)

# TO PRINT EACH LIST ELEMENT ALONG WITH ITS INDEX
for index,num in enumerate(nums):
    print(index,num)
# LIST TO STRING
new_courses = ','.join(courses)
print(new_courses)

# STRING TO LIST
coursess = new_courses.split(',')
print(courses)

# TUPLES
# THEY ARE SAME LIKE LIST BUT THEY ARE IMMUTABLE
empty_tuple_1 = []
empty_tuple_2=tuple()
list_1 = [1,2,3,4]
list_2  = list_1
print(list_1)
print(list_2)
list_1[0] = 0
print(list_1)
print(list_2)
list_3 = [1,2,3,4,5,6]
list_4 = [1,2,3,4,5,6]
print(list_3)
print(list_4)
list_3[0] = 0
print(list_3)
print(list_4)

# SETS
#UNORDERED
#UNIQUE VALUES
empty_set_1 = {} #THIS IS NOT A SET , IT'S A DICTIONARY
empty_set_2 = set()
empty_list_2=list()
games_1 = {'Cricket','Football','Volleyball'}
games_2 = {'Hockey','Football','Kabbadi'}

print('Cricket' in games_1)
print(games_1.intersection(games_2))
print(games_1.union(games_2))
print(games_1.difference(games_2))

