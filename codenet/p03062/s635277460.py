N = int(input())
*A, = map(int, input().split())

aA = [abs(a) for a in A]
asum = sum(aA)
c = sum([(a < 0) for a in A])

if c % 2:
	print(asum - min(aA) * 2)
else:
	print(asum)