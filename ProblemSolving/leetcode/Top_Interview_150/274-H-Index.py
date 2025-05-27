class Solution:
    def hIndex(self, citations) -> int:
        """
        Time complexity: O(n log n) due to sorting
        Space complexity: O(1) if we sort in place, O(n) if we use additional space
        """
        citations.sort(reverse=True)
        for i, c in enumerate(citations):
            if c < i+1:
                return i
        return len(citations)
    
    def hIndex2(self, citations) -> int:
        """
        Counting sort/Bucket sort approach
        Time complexity: O(n)
        Space complexity: O(n)
        """
        n = len(citations)
        bucket = [0] * (n+1)

        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        count = 0
        for i in range(n, -1, -1):
            count += bucket[i]
            if count >= i:
                return i
        return 0
        


if __name__ == "__main__":
    s = Solution()
    print(s.hIndex([3, 0, 6, 1, 5]))
