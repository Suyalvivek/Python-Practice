#SORTING A LIST
nums=[-1,2,-4,5,45]
# SORTED RETURNS A NEW LIST

nums_sorted = sorted(nums)
nums_sorted_abs = sorted(nums,key=abs)
print("Original List",nums)
print("Sorted List",nums_sorted)
print("Sorted List absolute",nums_sorted_abs)

# IN PLACE SORTING
nums.sort()
print("Sorted List",nums)
nums.sort(reverse=True)
print("Reverse Sorted List",nums)

# SORTING A TUPLE
tup = (1,3,4,5,-1)
tup_sorted = sorted(tup)
print("Tuple",tup)
print("Tuple Sorted List",tup_sorted)

# SORTING A DICTIONARY
d1 = {
    'name':'Vivek',
    'age':21,
    'job':'jobless'

}

# sorting in a dictionary means sorting by keys
d2 = sorted(d1)
print("Dictionary",d1)
print("Dictionary Sorted List",d2)