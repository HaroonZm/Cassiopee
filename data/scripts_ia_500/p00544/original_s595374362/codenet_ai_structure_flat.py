N, M = map(int, input().split())
A = []
cnt = 0
for i in range(N):
	s = input().strip()
	if i == 0:
		cnt += len(s) - s.count('W')
	elif i == N - 1:
		cnt += len(s) - s.count('R')
	else:
		A.append(s)
B = []
for w in range(N - 1):
	for b in range(1, N - w):
		r = N - 2 - w - b
		if r >= 0:
			B.append([w, b, r])
minmin = 2500
for b in B:
	cnt2 = 0
	for i in range(len(A)):
		if i < b[0]:
			cnt2 += len(A[i]) - A[i].count('W')
		elif i < b[0] + b[1]:
			cnt2 += len(A[i]) - A[i].count('B')
		else:
			cnt2 += len(A[i]) - A[i].count('R')
	if cnt2 < minmin:
		minmin = cnt2
print(cnt + minmin)