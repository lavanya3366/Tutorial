#enumerate is a built-in function in python that allows you to loop over a sequence(such as list,tuple or string)and get the index and value of ecah element in the sequence at the same time.
l1 = ["eat", "sleep", "repeat"]

# printing the tuples in object directly
for ele in enumerate(l1):
	print (ele)

# changing index and printing separately
for count, ele in enumerate(l1, 100):
	print (count, ele)

# getting desired output from tuple
for count, ele in enumerate(l1):
	print(count)
	print(ele)
