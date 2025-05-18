cnt = []
for _ in range(10**5+2):
	cnt.append(0)

n = int(input())
a = [int(v) for v in input().split()]

for x in a:
	cnt[x] += 1
	if x > 0 : cnt[x-1] += 1
	cnt[x+1] += 1
	
answer = 0
for n in cnt:
	answer = max(answer, n)

print(answer)