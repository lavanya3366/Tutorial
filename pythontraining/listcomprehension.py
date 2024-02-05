#list comprehension makes our code concise and readability
#without listcomprehension
# marks=[20,30,40,50,60]
# new_marks=[]
# for x in marks:
#     new_marks.append(x+2)
# print(new_marks)

#with list comprehension
# marks=[20,30,40,50,60]
# new_marks=[x+2 for x in marks]
# print(new_marks)

#without listcomprehension
# cubes=[]
# for x in range(10):
#     if x%2==0:
#         cubes.append(x**3)
# print(cubes)
#with listcomprehension

# cubes=[x**3 for x in range(10) if x%2==0]
# print(cubes)

#squaring number without list comprehension
# square=[]
# for x in range(1,10):
#     square.append(x**2)
# print(square)
#with listcomprehension
square=[x**2 for x in range(1,10)]
print(square)

