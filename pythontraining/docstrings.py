#docstrings are strings used right after the definition of a function,method,class,or module. They are used to documnet our code
#we can access these docstrings using the doc attribute
def square(n):
    '''takes in a number n,returns the square of n'''
    print(n**2)
square(5)
print(square.__doc__)

#PEP 8 -> Python Enhancement Proposal
#pep 8 is a document that provides guidelines and best practices on how to write python code.It was written in 2001.
#primary focus of pep 8 is to improve readibility and consistency of python code
#PEP is a document that describes new features proposed for python and documents aspects of python,like design and style,for the community

#ZEN of python-> import this