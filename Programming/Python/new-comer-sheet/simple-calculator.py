import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

x, y = [int(x) for x in input().split()]

print(x ,"+", y,"=", x+y)
print(x ,"*", y,"=", x*y)
print(x ,"-", y,"=", x-y)