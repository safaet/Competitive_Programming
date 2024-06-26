def printArray(arr, n):
    print("The reverse array is: ")
    for i in range(n):
        print(arr[i], end=" ")
    print()


def reverseArray(arr, n):
    p1 = 0
    p2 = n-1

    while p2 > p1:
        arr[p1], arr[p2] = arr[p2], arr[p1]
        p1 += 1
        p2 -= 1

    printArray(arr, n)

if __name__=='__main__':
    arr = [5, 4, 3, 2, 1]
    n = len(arr)
    reverseArray(arr, n)