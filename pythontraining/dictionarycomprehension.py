#without dictionarycomprehension
# dict={}
# for i in range(10):
#     if i%2==0:
#         dict[i]=i*i
# print(dict)

# dict1={i:i*i for i in range(10) if i%2==0}
# print(dict1)

#generating odd number cube without using list comprehension
# dict={}
# for x in range(1,10):
#     if x%2!=0:
#      dict[x]=x**3
# print(dict)

#with list comprehension
dict1={x:x**3 for x in range(1,10) if x%2!=0}
print(dict1)