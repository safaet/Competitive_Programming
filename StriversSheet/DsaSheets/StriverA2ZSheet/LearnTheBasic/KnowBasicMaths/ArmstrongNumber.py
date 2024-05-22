import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def isArmstriong(n):
    power = len(str(n))
    ans = 0

    for digit in str(n):
        ans = ans + (int(digit)) ** power

    return ans == n

a = int(input())

print(isArmstriong(a))
