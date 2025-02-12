class Solution:
	def merge(self, arr, l, m, r):
		n1 = m - l + 1
		n2 = r - m

		L = [0] * (n1)
		R = [0] * (n2)

		for i in range(0, n1):
			L[i] = arr[l + i]

		for j in range(0, n2):
			R[j] 