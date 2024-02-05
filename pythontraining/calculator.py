def calculator():
    a=int(input("enter first number"))
    b=int(input("enter first number"))
    op=input("enter operator")
    if(op=="+"):
        print(a+b)
    elif(op=="-"):
        print(a-b)
    elif(op=="*"):
        print(a*b)
    elif(op=="/"):
        print(a/b)
calculator()