# AOJ 0260: Salary for a Plumber
# Python3 2018.6.26 bal4u

while True:
	n = int(input())
	if n == 0: break
	p = list(map(int, input().split()))
	s = sum(p)
	j = list(map(int, input().split()))
	j.sort(reverse=True)
	ans = s*n
	for i in range(n-1):
		s += j[i]
		ans = max(ans, s*(n-1-i))
	print(ans)