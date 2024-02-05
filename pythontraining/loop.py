"""Equals: a == b
Not Equals: a != b
Less than: a < b
Less than or equal to: a <= b
Greater than: a > b
Greater than or equal to: a >= b"""

#short-hand if
#If you have only one statement to execute, you can put it on the same line as the if statement
a=10
b=20
if a > b: print("a is greater than b")
#Short Hand If Else
#If you have only one statement to execute, one for if, and one for else, you can put it all on the same line
a = 2
b = 330
print("A") if a > b else print("B")

#The and keyword is a logical operator, and is used to combine conditional statements
#we can also use->or,not operator
a = 200
b = 33
c = 500
if a > b and c > a:
  print("Both conditions are True")
  
#You can have if statements inside if statements, this is called nested if statements.
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

# if you for some reason have an if statement with no content, put in the pass statement to avoid getting an error
a = 33
b = 200

if b > a:
  pass

#Python has two primitive loop commands:while loops and for loops
#With the while loop we can execute a set of statements as long as a condition is true
i = 1
while i < 6:
  print(i)
  i += 1
  
#With the break statement we can stop the loop even if the while condition is true
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1
  
#With the else statement we can run a block of code once when the condition no longer is true
i = 1
while i < 6:
  print(i)
  i += 1
else:
  print("i is no longer less than 6")
  
#A for loop is used for iterating over a sequence( either a list, a tuple, a dictionary, a set, or a string)
fruits = ["apple", "banana", "cherry"]
for x in fruits:
  print(x)

#Even strings are iterable objects, they contain a sequence of characters
for x in "banana":
  print(x)

#The range() function returns a sequence of numbers, starting from 0 by default, and increments by 1 , and ends at a specified number
for x in range(6):
  print(x)

#The range() function defaults to increment the sequence by 1, however it is possible to specify the increment value by adding a third parameter: range(2, 30, 3)
for x in range(2, 30, 3):
  print(x)
  
#for loops cannot be empty, but if you for some reason have a for loop with no content, put in the pass statement to avoid getting an error.
for x in [0, 1, 2]:
  pass










