class Solution:

    def frequencyCount(self, arr, N, P):
        P += 1
        for i in range(N):
            idx = arr[i] % P
            if idx <= N:
                arr[idx-1] += P

        for i in range(N):
            arr[i] = arr[i]//P
        

arr = [2, 3, 2, 3, 5]
Solution().frequencyCount(arr, 5, 5) # 1

print(arr)
