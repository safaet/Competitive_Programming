def bubbleSort(arr, n):
        swapped = False
        cnt = 0

        for i in range(n):

            for j in range(0, n-i-1):
                if arr[j]> arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]
                    swapped = True
                    cnt = cnt +1

            if swapped == False:
                return -1
        return cnt

li = [1, 2, 3, 4, 5,6]

print(bubbleSort(li, len(li)))

