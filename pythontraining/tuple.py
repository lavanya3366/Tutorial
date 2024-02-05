#A tuple is a collection which is ordered and unchangeable
# creates a tuple which is immutable 
# tup = ('Geeks', 'For', 'Geeks') 
# print(tup) 
# #creation of nested tuple
# tuple=("points",[1,4,3],(7,3,6))
# print(tuple) 

#tuple can be created without any parentheses

#you must first convert tuple to list make changes in it and then convert list to tuple
# countries=("Spain","italy","india","england","germany")
# temp=list(countries)
# temp.append("Russia")
# temp.pop(3)
# temp[2]="Finland"
# countries=tuple(temp)
# print(countries)

#tuple unpacking is also possible
# tuple1=101,"anirban",20000.00,"hr department"
# print(tuple1)
# empid,empname,empsal,empdept=tuple1
# print(empid)
# print(empname)
# print(empdept)
# print(type(tuple1))

# #accessing element in a tuple
# tuple2=('w','e','l','c','o','m','e')
# print(tuple2)
# print(tuple[1])
# print(tuple[3])
# print(tuple2[5])

# #nested tuple
# nest_tuple2=("point",[1,3,4],(8,7,9))
# print(nest_tuple2)
# print(nest_tuple2[0][3])
# print(nest_tuple2[1][2])
# print(nest_tuple2[2][2])

# #slicing tuple contents
# tuple1=('w','e','l','c','o','m','e')
# print(tuple1[1:3])
# print(tuple1[:-3])
# print(tuple1[3:])
# print(tuple1[:])

#we can concatenate two tuples by using "+"operator

#methods -> count(),index()
tuple=(0,1,2,3,4,6,3,5,3,6,4)
res=tuple.index(3,6,9)
print(res)
