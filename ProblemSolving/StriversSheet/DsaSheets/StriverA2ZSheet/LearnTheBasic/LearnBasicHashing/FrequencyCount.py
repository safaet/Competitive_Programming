class Solution:

    def frequencyCount(self, arr, N, P):
        count = 0
        dic = {}
        for i in range(N):
            if i+1 not in dic:
                dic[i+1] = 0
            if arr[i] in dic:
                dic[arr[i]] +=1
            elif arr[i] <= N:
                dic[arr[i]] = 1

        li = sorted(dic.items())
        lis=[]

        for i in range(len(li)):
            arr[i] = li[i][1]

        
arr = [2, 3, 2, 3, 5]
Solution().frequencyCount(arr, 5, 5) # 1
print(arr)
