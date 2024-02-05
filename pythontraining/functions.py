#functions are reusable code and python uses def keyword to define a function
# def hello(): 
#    print("hello") 
#    print("hello again") 
# hello()

# # Python program to illustrate 
# # function with main 
def getInteger(): 
 result = int(input("Enter integer: ")) 
 return result 

def Main(): 
 print("Started") 

# # calling the getInteger function and 
# # storing its returned value in the output variable 
output = getInteger()	 
print(output) 

# # now we are required to tell Python 
# # for 'Main' function existence 
if __name__=="__main__": 
 Main()
 
# #Information can be passed into functions as arguments.
# def my_function(fname):
#   print(fname + " Refsnes")

# my_function("Emil")
# my_function("Tobias")
# my_function("Linus")

# #If the number of arguments is unknown, add a * before the parameter name
# def my_function(*kids):
#   print("The youngest child is " + kids[2])

# my_function("Emil", "Tobias", "Linus")

# def calculategreater(a,b):
#   if (a>b):
#     print("fist number is greater")
#   else:
#     print("second number is greater")
# a=9
# b=7
# calculategreater(a,b)
# c,d=10,11
# calculategreater(c,d)

#there are two types of functions->built-in,user-defined
#built-in->min(),max(),type(),tuple(),set(),print()