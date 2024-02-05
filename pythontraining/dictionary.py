#Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
#Dictionaries cannot have two items with the same key
#To determine how many items a dictionary has, use the len() function:

# creates a empty list 
Dict = [] 
  
# putting integer values 
# Dict = {1: 'Geeks', 2: 'For', 3: 'Geeks'} 
  
# print(Dict) 

# #The values in dictionary items can be of any data type:
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }

#accessing element from a dictioanry
# new_dict={1:"hello",2:"hi",3:"hola"}
# print(new_dict)
# print(new_dict[1])
# print(new_dict.get(20))

# #updating value
# new_dict[1]="hey"
# print(new_dict)

# #adding value
# new_dict[4]="namaste"
# print(new_dict)

# #creating a new dictionary
# squares={1:1,2:4,3:9,5:25}
# print(squares)

# #remove all items
# squares.clear()
# print(squares)

# #delete the dictioanry itself
# #del squares

#iterating throgh a dictioanry
squares={1:1,3:9,5:25,7:49,9:81}
for i in squares:
  print(squares[i])

