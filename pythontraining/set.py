#A set is a collection which is unordered, and unindexed
# define a set and its elements 
#as set doesn't have duplicate elements so, 1 geeks will not be printed 

#creating sets
# my_set1={11,33,66,55,44,22}
# print(my_set1)

#to create empty set
harry=set()
print(type(harry))

# #sets of mixed datatypes
# my_set2={101,"agnibha",(21,2,1994)}
# print(my_set2)

# #sets cannot have mutable items
# # my_set3={1,2,[3,4]}#error
# #we can make set from a list
# my_set4=set([1,2,3,2])
# print(my_set4)
# print(type(my_set4))

# #we can make list from set
# my_list1=list({11,22,33,44})
# print(my_list1)
# print(type(my_list1))

#operations on set
# my_set1={11,33,44,66,55}
# print(my_set1)
# #set object does not support indexing
# #add an element
# my_set1.add(77)
# print(my_set1)

# #add multiple element
# my_set1.update([88,99,22])
# print(my_set1)

# #add list and set
# my_set1.update([100,102],{103,104,105})
# print(my_set1)

# #discard an element which is not present,no error
# my_set1.discard(106)
# print(my_set1)

# #remove an element which is not present,error raised
# # my_set1.remove(6)
# # print(my_set1)

# #discard an element
# my_set1.discard(44)
# print(my_set1)
# my_set1.remove(55)
# print(my_set1)

#using pop()
# my_set2={11,22,33,44,55}
# print(my_set2)
# #pop an element
# print(my_set2.pop())
# #pop another element
# print(my_set2.pop()
# print(my_set2)

#union
myset1={0,1,2,3,4,5}
myset2={4,5,6,7,8,9}
# print(myset1.union(myset2))
# print(myset2 | myset1)
# #intersection
# print(myset1 & myset2)
# print(myset2.intersection(myset1))

#set difference 
# print(myset1-myset2)
# print(myset2.difference(myset1))

#symmetric difference->common elements will not come
print(myset1^myset2)
print(myset1.symmetric_difference(myset2))

#set membership
print(2 in myset1)

#iterating through a set
for letter in set("welcome"):
    print(letter)
    
#frozensets
#frozenset is a new class that has the characteristics
#of sets but its elements cannot be changed once assigned
#while tuples are immutable lists,frozensets are immutable sets
#initialize A and B
myset1=frozenset([1,2,3,4])
myset1.add(10)#error because frozenset is immutable







