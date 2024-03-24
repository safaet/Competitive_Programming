import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

x, y = [int(x) for x in input().split()]

sum = (x%10)+(y%10)

print(sum)