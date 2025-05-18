n = int(input())
c = 0
d,t = [0]*n,[0]*n
d[0],t[0] = map(int,input().split())
d[1],t[1] = map(int,input().split())

for i in range(2,n):
	d[i],t[i] = map(int,input().split())
	if d[i] == t[i] and d[i-1] == t[i-1] and d[i-2] == t[i-2]:
		c += 1
if c != 0:
	print('Yes')
else:
	print('No')