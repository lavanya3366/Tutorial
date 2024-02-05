def greet(fx):
    class NewClass(fx):
        def mfx(self):
            print("this is a new method added by decorator")
    return NewClass
@greet
class MyClass:
    def original_method(self):
        print("This is the original method")
obj=MyClass()
obj.original_method()
obj.mfx()
