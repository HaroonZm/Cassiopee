N = int(input())
li = []
for index in range(N-1):
	c, s, f = map(int, input().split())
	li.append((c, s, f))

for i in range(N):
	t = 0
	station = i
	while station < N-1:
		c, s, f = li[station]
		if t < s:
			t = s
			t += c
		else:
			t += (f-(t-s))%f + c
		station += 1
	print(t)