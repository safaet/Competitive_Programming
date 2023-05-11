import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

a = input()

if (int(a)%2== 0):
    print ("This is even number\n")
else:
    print("This is odd number\n")