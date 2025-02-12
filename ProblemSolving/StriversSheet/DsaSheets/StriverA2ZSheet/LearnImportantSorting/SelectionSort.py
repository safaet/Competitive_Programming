
class Solution: 
    def select(self, arr, i):
        pass
    
    def selectionSort(self, arr,n):
        for i in range(n):
            minIndex = i
            for j in range(i+1, n):
                if arr[j] < arr[minIndex]:
                    minIndex = j
            arr[i], arr[minIndex] = arr[minIndex], arr[i]



if __name__ == '__main__': 
    t = int(input())
    for _ in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        Solution().selectionSort(arr, n)
        for i in range(n):
            print(arr[i],end=" ")
        print()
