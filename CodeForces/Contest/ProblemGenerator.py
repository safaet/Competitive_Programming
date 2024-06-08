import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

def solve(m, s):
    ns = 'ABCDEFG'
    fs = ns * m
    ans = len(fs)

    for i in range(len(s)):
        if s[i] in fs:
            ans = ans -1
            fs = fs.replace(s[i], '', 1)
    return ans


if __name__ == "__main__":
    t = int(input())
    while t>0:
        n, m = map(int, input().split())
        s = input()
        print(solve(m, s))
        t = t-1
