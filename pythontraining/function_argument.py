#default,keyword,variable length,required arguments
# def average(a=9,b=1):#default argument
#     print("the average is",(a+b)/2)
# average(b=9)

# def name(fname,mname="Jhon",lname="Whatson"):
#     print("Hello,",fname,mname,lname)
# name("Amy","Agarwal")

# #keyword argument->we can provide arguments with key=value,this way the interpreter recognizes the arguments by the parameters name. Hence,the order in which the arguments are passed does not matter.

# #required arguments->in case we dont't pass the arguments with a key=value syntax,then it is necessary to pass the arguments in the correct positional order and the number of arguments passed should match with actual function definition.
# def name(fname,midname,lastname="watsone"):
#     print("hello",fname,midname,lastname)
# name("Amy","John")

#variable length
# def name(*arg):
#     sum=0
#     for i in arg:
#         sum=sum+i
#     avg=sum/len(arg)
#     print(avg)
# name(1,2,3,4,5,9)

def name(**args):
    print("hello,",args["fname"],args["mname"],args["lname"])
name(mname="buchanan",lname="barnes",fname="james")
        
