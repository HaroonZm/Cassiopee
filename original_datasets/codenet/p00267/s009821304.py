# AOJ 0272: The Lonely Girl's Lie
# Python3 2018.6.26 bal4u

def counting_sort(nmax, la):  # nmax:最大値, n:len(la), a:データリスト
	f = [0]*(nmax+1)
	nmax = 0
	for a in la:
		f[a] += 1
		if a > nmax: nmax = a
	k, i = len(la), nmax
	la = []
	while k:
		if f[i]:
			la += [i]*f[i]
			k -= f[i]
		i -= 1
	return la
	
while True:
	n = int(input())
	if n == 0: break
	a = list(map(int, input().split()))
	b = list(map(int, input().split()))
	a = counting_sort(100000, a)
	b = counting_sort(100000, b)
	ans, i = n, -1
	for k in range(0, n, 2):
		i += 1
		if a[k] > b[i]:
			ans = k + 1
			break
	print("NA" if ans == n else ans)