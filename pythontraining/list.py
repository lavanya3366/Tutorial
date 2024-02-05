#  List is a mutable data structure i.e items can be added to list later after the list creation.
# Python program to illustrate a list  
  
# creates a empty list 
nums = []  
  
# appending data in list 
nums.append(21) 
nums.append(40.5) 
nums.append("String") 
  
print(nums) 

"""List items are ordered, changeable, and allow duplicate values.

List items are indexed, the first item has index [0], the second item has index [1] etc."""

#To determine how many items a list has, use the len() function:
thislist = ["apple", "banana", "cherry"]
print(len(thislist))


#A list can contain different data types
list1 = ["abc", 34, True, 40, "male"]

#lists are defined as objects with the data type 'list'
mylist = ["apple", "banana", "cherry"]
print(type(mylist))

#It is also possible to use the list() constructor when creating a new list.
thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
print(thislist)

#List items are indexed and you can access them by referring to the index number
"""Negative indexing means start from the end
-1 refers to the last item, -2 refers to the second last item etc"""
thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

print(thislist[2:5])
#and note that the item in position 5 is NOT included

#To determine if a specified item is present in a list use the in keyword
thislist = ["apple", "banana", "cherry"]
if "apple" in thislist:
  print("Yes, 'apple' is in the fruits list")
  
#To change the value of a specific item, refer to the index number
"""To add an item to the end of the list, use the append() method
To insert a list item at a specified index, use the insert() method
To append elements from another list to the current list, use the extend() method
The extend() method does not have to append lists, you can add any iterable object (tuples, sets, dictionaries)"""

"""The remove() method removes the specified item.
The pop() method removes the specified index
If you do not specify the index, the pop() method removes the last item
The del keyword also removes the specified index
The clear() method empties the list"""




