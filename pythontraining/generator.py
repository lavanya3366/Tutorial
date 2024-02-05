"""generator is special type of function that allow you to create an iterable sequence of values. A generator function return a generator object which can be used to generate the values one by one as you iterate over it
generator is powerful tool for working with large and complex data sets,as they allow you to generate the value on-the-fly,rather than having to create and store the entire sequence in memory"""
"""in python you can create generator by using yield statement
the yield statement returns a value from the generator and suspends the execution of the function until the next value is requested"""
def my_generator():
    for i in range(500):
       yield i
gen=my_generator()
# print(next(gen))
for j in gen:
   print(j) 
   
"""another benefit of generotor is that they are lazy that is that the values are generated when they are requested.
this allows you to generate the values in a more efficient and memory friendly manner ,as you dont have to generate all the values up front"""
        