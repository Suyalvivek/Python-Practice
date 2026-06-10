"""
## Exercise: Numbers in python
1. You have a football field that is 92 meter long and 48.8 meter wide. Find out total
area using python and print it.
2. You bought 9 packets of potato chips from a store. Each packet costs 1.49 dollar
and you gave shopkeeper 20 dollar. Find out using python, how many dollars is the shopkeeper going to give you back?
3. You want to replace tiles in your bathroom which is exactly square and 5.5 feet
is its length. If tiles cost 500 rs per square feet, how much will be the total
cost to replace all tiles. Calculate and print the cost using python
(Hint: Use power operator ** to find area of a square)
4. Print binary representation of number 17

"""
field_len = 92
field_width=48.8
area = field_len * field_width
print(area)

gave=20
packet=9
cost_per_pack=1.49
total_cost=packet * cost_per_pack
return_amount= gave-total_cost
print(return_amount)

cost_per_sqft=500
area_tile=5.5*5.5
total_cost = cost_per_sqft * area_tile
print(total_cost)

print("Binary rep of num 17 is ",format(17,'b'))
