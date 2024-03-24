import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = int(input())
s = 0

a = list(map(int, input().strip().split()))[:n]

s = sum(a)
	
print(abs(s))