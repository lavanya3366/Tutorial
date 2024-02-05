#decorators are functions which changes one function and then return it
#decorator is a function that take another function as an argument and returns a new function that modifies the behavior of the original function. The new function is often referred to as a"decorated" function
# def greet(fx):
#     def mfx():
#         print("good morning")
#         fx()
#         print("thanks")
#     return mfx
# @greet
# def hello():
#     print("hello world")
# # hello()

# def greet(fx):
#     def mfx(*args,**kwargs):
#         print("good morning")
#         fx(*args, **kwargs)
#         print("thanks")
#     return mfx
# @greet
# def add(a,b):
#     print(a+b)

# add(1,2)
# def hello():
#     print("hello world")
# hello()

def hello_decorator(func):
    def inner1():
        print("Hello, this is before function execution")
        func()
 
        print("This is after function execution")
         
    return inner1
def function_to_be_used():
    print("This is inside the function !!")
function_to_be_used = hello_decorator(function_to_be_used)
function_to_be_used()