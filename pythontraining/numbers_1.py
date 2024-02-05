#python supports three number data types->integer,floating,complex
#0b or 0B as binary
#0o or 0O as octal number
#0x or 0X as hexadecimal number prefix

#isinstance()->return true or false
print(0b1101)
print(0xab)
print(0o23)

#python decimal
data1=0.1+0.2
print(data1)
from decimal import Decimal as D
print(D('0.1')+D('0.2'))

#fraction
from fractions import Fraction as F
print(F(1.5))
print(F(5))
print(F(1,5))
print(F(5,6))

#python math module ->cos,log,pi,log20,factorial,sinh,exp

#python random module
import random
print(random.randrange(5,15))

day=['Sun','mon','tue','wed','thur','fri','sat']
print(day)
print(random.choice(day))

random.shuffle(day)
print(day)
#print random element
print(random.random())