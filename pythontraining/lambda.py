"""def double(x):
 return x*2"""

#A lambda function is a small anonymous function
double=lambda x:x*2
cube=lambda x,y,z:(x+y+z)/2
print(double(5))
print(cube(2,3,4))
#we can use anonymous function inside another function
def myfunc(n):
  return lambda a : a * n

mydoubler = myfunc(2)

print(mydoubler(11))
