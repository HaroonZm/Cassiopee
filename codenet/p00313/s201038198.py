def inp2list():
	tmp=list(map(int, input().split()))
	del tmp[0]
	return tmp

N = int(input())
A, B, C = inp2list(), inp2list(), inp2list()
R = [False for _ in range(N)]
for i in C:
	if A.count(i)==0 or B.count(i)!=0:
		R[i-1] = True

print(R.count(True))