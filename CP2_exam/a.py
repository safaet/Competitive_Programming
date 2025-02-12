def Solution(N):

	r = N % 3

	if r == 1 or r == 2:
		return [1, 2]

	else:
		return [0, 0]


t = int(input())
for i in range(t):
	N = int(input())

	print(Solution(N))
	