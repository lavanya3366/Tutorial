#shallow copy->copy.copy
#deep copy->copy.deepcopy
#shallow copy creates a copy of the object but reference each element of the object
#deep copy creates a copy of the object and the elements of the objects
import copy
old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(old_list)
new_list[0]=['a','b','c']
print("old list:",old_list)
print("new list:",new_list)

old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.copy(old_list)
new_list[0][2]='a'
print("old list:",old_list)
print("new list:",new_list)

old_list=[[1,2,3],[4,5,6],[7,8,9]]
new_list=copy.deepcopy(old_list)
new_list[0][2]='a'
print("old list:",old_list)
print("new list:",new_list)