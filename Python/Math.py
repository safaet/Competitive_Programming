import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

import math
a = 25
b = 4
add = a + b
subt = a-b
mul = a*b
quet = a/b
rem = a%b

power = pow(2, 2)
print("addition of a and b is = ",add)
print("Substraction of a and b is = ",subt)
print("Multiplication of a and b is = ", mul)
print("Quetetion of a and b is = ", quet)
print("Floor value of quetion is = ", math.floor(6.25))
print ("remainder of a and b is = ", rem)
print("Power value of 2 and 2 is = ",power)