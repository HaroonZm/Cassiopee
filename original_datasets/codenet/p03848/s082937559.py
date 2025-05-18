N = int(input())
A = [int(i) for i in input().split()]
A.sort()
A.reverse()
if N % 2:
	B = [i for i in range(2,N,2)]*2
	B.sort()
	B.reverse()
	B.append(0)
else:
	B = [i for i in range(1,N,2)]*2
	B.sort()
	B.reverse()
if A == B:
	ans = 2**(N//2)
else:
	ans = 0
print(ans%(10**9+7))