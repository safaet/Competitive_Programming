import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

a, b, c, d = [int(x) for x in input().split()]

dif = (a*b) - (c*d)

print("Difference =",dif)