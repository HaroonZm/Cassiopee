n, k = map(int, input().split())

k_max = (n-1)*(n-2)//2
if k > k_max:
	print(-1)
	exit()

m = (n-1) + k_max - k
print(m)

for i in range(n-1):
	print(1, i+2)
ptr1 = 2
ptr2 = 3
for _ in range(k_max - k):
	print(ptr1, ptr2)
	if ptr2 < n:
		ptr2 += 1
	else:
		ptr1 += 1
		ptr2 = ptr1 + 1