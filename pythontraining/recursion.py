# def factorial(n):
#     if (n==0 or n==1):
#         return 1
#     else:
#         return n * factorial(n-1)
# print(factorial(3))

def fibonnaci(n):
    if n<0:
        print("incorrect input")
    elif n==0:
        return 0
    elif n==1 or n==2:
        return 1
    else:
        return fibonnaci(n-1)+fibonnaci(n-2)
print(fibonnaci(9))
     