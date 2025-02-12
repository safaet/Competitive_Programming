t = int(input())
li = []
a = False

for i in range(t):
    s = input()
    li.append(s)

fs = input()
li = sorted(li)

for i in range(t):
    if fs == li[i]:
        print(i+1)
        a = True
        break

if a == False:
    print(-1)