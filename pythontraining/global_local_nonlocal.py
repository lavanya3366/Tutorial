#global and local variable with different name
# x="global"
# def func1():
#     #global x
#     x="global"
#     y="local"
#     x=x*2
#     print(x)
#     print(y)
# print("global x=",x)
# func1()
# print("global x=",x)

#global and local varibale with same name
# a=5
# def func1():
#     #global a
#     a=4#local varibale with same name as of global variable
#     print("local a:",a)
# print("global a:",a)
# func1()
# print("global a:",a)
    
def outer():
    x="local"
    def inner():
        nonlocal x
        x="nonlocal"
        print("inner function x: ",x)
    inner()
    print("outer:",x)
outer() #output : local
    