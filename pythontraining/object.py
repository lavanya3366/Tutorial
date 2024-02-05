# class MyComplexNumber:
#     def __init__(self, real=0, imag=0):
#         print("MyComplexNumber constructor executing...")
#         self.real_part=real
#         self.imag_part=imag
#     def displayComplex(self):
#         print("{}+{}j".format(self.real_part,self.imag_part))
# complx1= MyComplexNumber(40,50)
# complx1.displayComplex()
# complx2=MyComplexNumber(60,70)
# complx2.new_attribute=80
# print((complx2.real_part,complx2.imag_part,complx2.new_attribute))
# print(complx1)
# #to delete object complx1
# del complx1.real_part
# del complx1
# print(complx1)

#class
class ExampleClass:
    def function1(parameters):
        print("functions1()executing...")
    def function2(parameters):
        print("function2()executing..")
ob1=ExampleClass()
ob1.function1()
ob1.function2()