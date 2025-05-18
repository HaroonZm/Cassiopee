n = int(input())
a = list(map(int,input().split()))

ans = 10 ** 7
sum = 0
for i in range(n):
	sum+=a[i]
	ans = min(ans,sum // (i + 1))
print(ans)