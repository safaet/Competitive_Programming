import heapq

nums = [16, -13, -5, -10, 4, 3, 9]
k = 2

heap = [(-nums[0], 0)]
print(heap)
ans = nums[0]
print(ans)


for i in range(1, len(nums)):

    while i - heap[0][1] > k:
        heapq.heappop(heap)
    print(i)

    curr = max(0, -heap[0][0]) + nums[i]
    ans = max(ans, curr)
    heapq.heappush(heap, (-curr, i))
