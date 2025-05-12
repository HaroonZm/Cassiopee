from collections import deque
used = [0]*(3**10)

while True:
	s = raw_input()
	if s=="0":
		break
	n=len(s)
	t=0
	for i in range(len(s)):
		t*=3
		if s[i]=="r":
			t+=0
		if s[i]=="g":
			t+=1
		if s[i]=="b":
			t+=2
	f=0
	for i in range(3**n):
		used[i]=0
	tq=[t]
	q=deque(tq)
	used[t]=1
	ans=-1
	cnt=0
	while len(q)>0:
		qs=len(q)
		for o in range(qs):
			top=q.popleft()
			v=[0]
			v.pop()
			for i in range(n):
				v.append(top%3)
				top/=3
			ok=1
			a=v[0]
			for i in range(n):
				if v[i]!=a:
					ok=0
			if ok==1:
				f=1
				ans=cnt
				break
			for i in range(n-1):
				if v[i]!=v[i+1]:
					t1=v[i]
					t2=v[i+1]
					v[i]=3-t1-t2
					v[i+1]=3-t1-t2
					tmp=0
					for j in range(n):
						tmp*=3
						tmp+=v[j]
					if used[tmp]==0:
						q.append(tmp)
						used[tmp]=1
					v[i]=t1
					v[i+1]=t2
		if f==1:
			break
		else:
			cnt+=1
	if ans==-1:
		print "NA"
	else:
		print ans