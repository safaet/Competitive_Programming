# import sys
# sys.stdout = open('output.txt', 'w')
# sys.stdin = open('input.txt', 'r')

t = int(input())

for i in range(t):
    t = t-1
    n, m, k = [int(x) for x in input().split()]

    x, y = [int(x) for x in input().split()]

    ans = "YES"

    for i in range(k):
        xx, yy = [int(x) for x in input().split()]

        if(x+y) % 2 ==(xx+yy)%2:
            ans = "NO"

    print(ans)