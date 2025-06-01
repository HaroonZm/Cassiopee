while True:
	n = int(input())
	if n == 0:
		break
	C = [int(input())]
	L = [1]
	for i in range(1, n):
		c = int(input())
		if C[-1] == c:
			L[-1] += 1
		else:
			C.append(c)
			L.append(1)
	m = len(C)
	ret = 0
	for i in range(m):
		L[i] -= 1
		if i + 1 < m:
			L[i + 1] += 1
			low, hih = (i, i + 1) if L[i] > 0 else (i - 1, i + 1)
			tmp = 0
			if 0 <= low and L[low] >= 4 and (hih >= m or C[low] != C[hih]):
				tmp += L[low]
				low -= 1
			if hih < m and L[hih] >= 4 and (low < 0 or C[low] != C[hih]):
				tmp += L[hih]
				hih += 1
			while 0 <= low and hih < m and C[low] == C[hih] and L[low] + L[hih] >= 4:
				tmp += L[low] + L[hih]
				low -= 1
				hih += 1
			if tmp > ret:
				ret = tmp
			L[i + 1] -= 1
		if i - 1 >= 0:
			L[i - 1] += 1
			low, hih = (i - 1, i) if L[i] > 0 else (i - 1, i + 1)
			tmp = 0
			if 0 <= low and L[low] >= 4 and (hih >= m or (hih < m and C[low] != C[hih])):
				tmp += L[low]
				low -= 1
			if hih < m and L[hih] >= 4 and (low < 0 or (low >= 0 and C[low] != C[hih])):
				tmp += L[hih]
				hih += 1
			while 0 <= low and hih < m and C[low] == C[hih] and L[low] + L[hih] >= 4:
				tmp += L[low] + L[hih]
				low -= 1
				hih += 1
			if tmp > ret:
				ret = tmp
			L[i - 1] -= 1
		L[i] += 1
	print(n - ret)