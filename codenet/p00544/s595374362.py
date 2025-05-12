def getPaintCount(string, color):
	return len(string)-string.count(color)

N, M = map(int, input().split())
A = []
cnt = 0
for i in range(N):
	s = input().strip()
	if i==0:  #1行目は白
		cnt += getPaintCount(s, 'W')
	elif i==N-1:  #最終行は赤
		cnt += getPaintCount(s, 'R')
	else:
		A.append(s)  #N-2行のリスト

B = []  #白、青、赤の行数の組み合わせリスト
for w in range(0, N-1):  #白は0からN-3行の可能性
	for b in range(1, N-w):  #青は1からN-2行の可能性
		r = N-2-w-b
		if r>=0: B.append([w, b, N-2-w-b])
#print(B)
minmin = 2500
cnt2 = 0
for b in B:
	for i in range(len(A)):
		if i<b[0]:
			cnt2 += getPaintCount(A[i], 'W')
		elif b[0]<=i<b[0]+b[1]:
			cnt2 += getPaintCount(A[i], 'B')
		elif b[0]+b[1]<=i<b[0]+b[1]+b[2]:
			cnt2 += getPaintCount(A[i], 'R')
	if cnt2<minmin:
		minmin = cnt2
	cnt2 = 0

print(cnt+minmin)