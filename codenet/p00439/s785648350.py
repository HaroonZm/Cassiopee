a, s = [0]*100003, [0]*100003
while True:
	n, k = map(int, input().split())
	if n == 0: break
	s[0] = a[0] = int(input())
	for i in range(1, n):
		a[i] = int(input())
		s[i] = s[i-1] + a[i]
		if i >= k: s[i] -= a[i-k]
	ans = s[k-1]
	for i in range(k, n):
		if s[i] > ans: ans = s[i]
	print(ans)