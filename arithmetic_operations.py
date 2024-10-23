#declared two integers a and b with random values and performing arithmetic operations 
a=7
b=3
print(a+b,a-b,a*b,a/b,a%b,a//b,a**b,complex(a,b),sep='\n')

'''+ for addition,- for subtraction,* for product, / for division(quotient), % for remainder, // for floor division or integer division, 
complex() for complex numbers '''
'''round() for rounding off to particular decimal places'''
print(a//b,-(-a//b)) #floor and ceil respectively!!!,for floor and ceil use math module


#mathematical functions
from math import ceil,floor,pow,sqrt  # other commonly used ones are pi, inf, nan(not a number), gcd, factorial and trignometric functions
from operator import add,sub,truediv,mod,mul,floordiv,pow #other functions are lt,gt,le,ge,eq,ne (less than,greater than....)
print(add(2,1),sub(2,1),truediv(2,1),mod(2,1),mul(2,1),pow(2,1),floordiv(3,2),sep='\n')
print("Math functions---")
print(sqrt(3),pow(2,3),ceil(4.4),floor(4.7),sep="\n")
print("Round function")
print(round(4.4),round(4.7),sep='\n') #less than 0.5 returns floor value, greater than 0.5 returns ceil value




