import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

n = 641009859
sum = n * (n + 1) / 2
print(sum)