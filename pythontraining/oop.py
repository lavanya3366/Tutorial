#self parameter is a reference to the current instance of the class, and is used to access variables that belong to the class
#it must be provided as the extra parameter inside the method definition
class Details:
    name="lavanya"
    department="IT"
    def desc(self):
        print(f"{self.name} is in {self.department}")
obj1=Details()
obj1.name="Raj"
obj2=Details()
obj2.name="harry"
obj1.desc()
obj2.desc()