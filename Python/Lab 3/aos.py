from cmath import sqrt
import math
import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

pi = 22/7

radius = input('Enter radius = ')
angle = input('\nEnter angle = ')

sector = (float(pi) * int(radius) * int(radius)) * (int(angle) / 360)
print("\nArea of sector is = ", sector) 