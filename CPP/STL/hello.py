import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

print('hello')

a = 10
b = 15
sum = a + b

print (sum) 