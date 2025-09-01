num_list = [10,2,5,7,20,76]
num_list.insert(2,450)
print(num_list)
num_list.pop(0)
print(num_list)
num_list.sort(reverse=True)
print(num_list)
num_list.append(45)
print(num_list)

print("slicing: \n\n")
num_list_2 = [x*10 for x in range(1,7)]
print(num_list_2)
print(num_list_2[-len(num_list_2)::])
num_list_3 = [x for x in range(1,11)]

print(num_list_3[1::2])

import array as arr

nums = arr.array("B", num_list_3)

# Create a multiplication table for the 5X table using only lists and list methods (no loops)

# 

# Find and print the following

#

# Print the full list

# Remove one value from the list

# insert a number back in the correct place

# Remove the last value

# Print the 5th element

# Find the position of 40 in the list

# Count how many times 5 appears in the list

fives = [x*5 for x in range(1,13)]

print(fives)
del fives[1]
print("10 removed:")
print(fives)
fives.insert(1,10)
print("10 added:")
print(fives)
fives.pop()
print("last value removed")
print(fives)
print("index 4:")
print(fives[4])
print("index of 40")
print(fives.index(40))
print("number of occurences of 5:")
print(fives.count(5))