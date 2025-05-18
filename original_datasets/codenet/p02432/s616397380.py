from collections import deque
q=int(input())
lis=deque()
lq=[]
for i in range(q):
	lq.append([int(x) for x in input().split(' ')])

for i in lq:
	order=i[0]
	if order==0:
		d=i[1]
		if d==0:
			lis.appendleft(i[2])
		else:
			lis.append(i[2])
	elif order==1:
		print(lis[i[1]])
	elif order==2:
		d=i[1]
		if d==0:
			lis.popleft()
		else:
			lis.pop()