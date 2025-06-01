def myinput(n):
	C=[int(input())]
	L=[1]
	for i in range(1,n):
		c = int(input())
		if C[-1] == c:
			L[-1]+=1
		else:
			C.append(c)
			L.append(1)
	return [C,L]

def check(C,L,low, hih):
	m = len(C)
	ret = 0
	if 0<=low and L[low]>=4 and (hih>=m or C[low] != C[hih]):
		ret += L[low]
		low -= 1
	if hih<m and L[hih]>=4 and (low<0 or C[low] != C[hih]):
		ret += L[hih]
		hih += 1
	while 0 <= low and hih < m and C[low] == C[hih] and L[low] + L[hih] >= 4:
		ret += L[low] + L[hih]
		low -= 1
		hih += 1
	return ret

def solve(C,L):
	m = len(C)
	ret = 0
	for i in range(m):
		L[i]-=1
		if i+1 < m:
			L[i+1]+=1
			if L[i]>0:
				ret = max(ret, check(C, L, i  , i+1))
			else:
				ret = max(ret, check(C, L, i-1, i+1))
			L[i+1]-=1
		if i-1 >= 0:
			L[i-1]+=1
			if L[i]>0:
				ret = max(ret, check(C, L, i-1, i))
			else:
				ret = max(ret, check(C, L, i-1, i+1))
			L[i-1]-=1
		L[i]+=1
	return ret

while True:
	n = int(input())
	if n == 0:
		break
	C,L = myinput(n)
	print(n - solve(C,L))