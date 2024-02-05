#the process of converting the value to one data type to another data type(integer,string,float etc).
#two types of type conversions are->implicit and explicit type conversion

#implicit 
# num_int=123
# num_float=1.23
# num_new=num_int+num_float
# print(type(num_int))
# print(type(num_float))
# print(type(num_new))

#explicit type conversion
num_int=123
num_str="456"
print(type(num_int))
print(type(num_str))
num_str=int(num_str) #converting string to int
print(type(num_str))
num_sum=num_int+num_str
print(num_sum)
