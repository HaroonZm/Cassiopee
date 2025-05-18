n = int(raw_input())
a = [int(x) for x in raw_input().split()]

a.sort()

s = a[0]
m = 0
for i in xrange(1, n):
	if s * 2 < a[i]:
		m = i
	s += a[i]

print(n - m)