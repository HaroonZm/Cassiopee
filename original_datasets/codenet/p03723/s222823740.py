A, B, C = map(int, input().split())

if any([A % 2, B % 2, C % 2]):
	print(0)
	exit()

if A == B == C:
	print(-1)
	exit()

count = 0
while True:
	if any([A % 2, B % 2, C % 2]):
		break
	A, B, C = B // 2 + C // 2, A // 2 + C // 2, A // 2 + B // 2
	count += 1
print(count)