from cmath import sqrt
import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

a = input()
b = input()
c = input()
s = (int(a) + int(b) + int(c)) / 2

area = math.sqrt(float(s) * (float(s) - int (a))*(float(s) - int (b))*(float(s)- int(c)))
print(area)