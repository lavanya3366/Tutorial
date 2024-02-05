# #as
# import math as myMath
# print(myMath.cos(myMath.pi))
# #assert
# assert 5>4
# assert 5<4 #assertionerror

# for i in range(5):
#     # Some condition
#     if i == 3:
#         pass  # No operation for this iteration
#     else:
#         print(i)
        
#try..raise...catch...finally
# try:
#     x=9
#     #raise ZeroDivisionError
# except ZeroDivisionError:
#     print("division cannot be performed")
# finally:
#     print("execution successfully")
    
# #from...import 
# import math
# from math import cos
# print(cos(10))

#nonlocal
def outer_function():
    a=5
    def inner_function():
        nonlocal a
        a=10
        print("inner function: ",a)
    inner_function()
    print("outer function: ",a)
outer_function()



