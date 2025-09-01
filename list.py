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