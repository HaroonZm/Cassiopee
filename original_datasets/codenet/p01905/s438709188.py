# AOJ 2805: Tournament
# Python3 2018.7.11 bal4u

def calc(l, n):
	if n == 2:
		if a[l] and a[l+1]: return [0, True]
		if a[l] or a[l+1]: return [0, False]
		return [1, False]
	m = n >> 1
	c1, f1 = calc(l, m)
	c2, f2 = calc(l+m, m)
	if f1 and f2: return [c1+c2, True]
	if f1 or f2: return [c1+c2, False]
	return [c1+c2+1, False]

N, M = map(int, input().split())
if M == 0: print(N-1)
else:
	a = [False]*256
	for i in range(M): a[int(input())] = True
	print(calc(0, N)[0])