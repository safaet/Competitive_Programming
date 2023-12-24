import sys
sys.stdout = open('output.txt', 'w')
sys.stdin = open('input.txt', 'r')

t = int(input())

while (t>0):
    print(t)
    n = int(input())
    li = []
    a, b, c = 1, 2, 3

    while(len(li) != n):
        if (3*c % (a+b) != 0):
            #if(len(li) == 0):
            li.append(a)
            li.append(b)
            li.append(c)
            #else:
             #   li.append(c)
        
        else:
            a+=1
            b+=1
            c+=1
    print(li)

    t = t-1