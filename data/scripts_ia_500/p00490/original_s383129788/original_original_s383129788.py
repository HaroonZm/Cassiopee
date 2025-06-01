# AOJ 0567: Best Pizza
# Python3 2018.6.30 bal4u

n = int(input())
a, b = map(int, input().split())
c = int(input())
ans, p = c/a, a
d = [int(input()) for i in range(n)]
d.sort(reverse=True)
for i in range(n):
	t = (c+d[i])/(p+b)
	if t > ans:
		ans = t
		c += d[i]
		p += b
	else: break;
print(int(ans))