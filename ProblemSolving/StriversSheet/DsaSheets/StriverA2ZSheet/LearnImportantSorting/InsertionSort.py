class Solution:
    def insert(self, alist, index, n):
        #code here
        pass
        
    #Function to sort the list using insertion sort algorithm.    
    def insertionSort(self, arr, n):
        #code here
        for i in range(1, len(arr)):

            key = arr[i]
    
            # Move elements of arr[0...i-1], that are 
            # greater than key, to one position ahead
            # of their current position
            j= i-1
            while j >= 0 and key < arr[j]:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = key


#{ 
 # Driver Code Starts

if __name__=="__main__":
    t=int(input())
    for i in range(t):
        n=int(input())
        arr=list(map(int,input().split()))
    
        Solution().insertionSort(arr,n)
    
        for i in range(n):
            print(arr[i],end=" ")
    
        print()