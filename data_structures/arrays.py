# python stores pointers to values in contiguous space
# values are stored else where
# arrays in python are lists
new_list = [5,1,3,2,6]

# result = new_list[0]
# print(result)

# force index error
# result_error = new_list[5]
# print(result_error)

# in operator calls a contains operation which runs a linear search
# if 1 in new_list: print(True)

# linear search
# for n in new_list:
#   if n ==1:
#     print(True)
#     break
numbers = []
numbers.append(2)
numbers.append(1) # list size was 1, but needs more memory. memory allocation increased by calling a list resize operation
print(numbers)
numbers.extend([4,5,6])
print(numbers)