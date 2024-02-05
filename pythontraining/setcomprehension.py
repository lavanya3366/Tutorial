# input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
# output_set = set()
# for var in input_list:
# 	if var % 2 == 0:
# 		output_set.add(var)
# print(output_set)
#with set comprehension
input_list = [1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 7]
output_set={var for var in input_list if var%2==0}
print(output_set)
