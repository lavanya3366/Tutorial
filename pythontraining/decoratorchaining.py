def decor1(func):
    def inner():
        x=func()
        return x*x
    return inner
def decor(func):
    def inner():
        x=func()
        return x*2
    return inner
@decor1
@decor
def num():
    return 10
print(num())
