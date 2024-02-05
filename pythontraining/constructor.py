#constructor is aspecial method in a class used to create and initialize an object of a class. There are different types of constructors. Constructor is invoked automatically when object of class is created.
#main purpose of constructor is to initialize or assign values to the data members of that calss. 
#It cannot return any value other than none
class Person:
    def __init__(self,n,o):
        print("hey i am a person")
        self.name=n
        self.occ=o
    def info(self):
        print(f"{self.name} is a {self.occ}")
a=Person("harry","developer")
b=Person("Divya","HR")
a.info()
b.info()
