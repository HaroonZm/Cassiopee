N = int(input())
Ss = input().split()
res = 1
for t in range(1, N+1):
	if (N%t != 0): continue
	f = False
	for i in range(N-t):
		if (Ss[i] == Ss[i + t]): continue
		f = True
		break
	if (f): continue
	res = N // t
	break

print(res)