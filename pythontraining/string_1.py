#ACCESSING the character in a string 
# mystr='language'
# print('mystr=',mystr)
# print('mystr[0]',mystr[0])
# print('mystr[7]',mystr[7])
# print('mystr[1:5]',mystr[1:5])

# #strings are immutable
# #but different strings can be assigned
# mystr='language'
# print(mystr)
# mystr='programming'
# print(mystr)

#iterating through a string 
# letter_count=0
# for letters in 'hello world':
#     if(letters == 'l'):
#         letter_count += 1
# print(letter_count,'times 1 letter has been found')

#built-in function
mystr='university'
#using enumerate()
my_list_enumerate=list(enumerate(mystr))
print(my_list_enumerate)
#using character count
print('len(mystr)=',len(mystr))

#string formatting using escape sequence
#print("tell me "what's your name?"")

#using triple quotes
print('''tell me "what's your name?"''')

#escaping single quotes
print('tell me "What\'s your name?"')

#escaping single quote
print("tell me 'What\'s your name'")

print("ABC written in \x41\x42\x43(HEX) representation")

#format() method
default_order="{} {} and {}".format('Today','is','Sunday')
print(default_order)

#formatting numbers
print("Required binary representation of {0} is {0:b}".format(20))

#formatting floats
print("exponent representation: {0:e}".format(1566.345))

#round off
print("one third is:{0:3f}".format(1/3))

#lowe,upper,find,replace
print("good morning to all".replace('all','everybody'))