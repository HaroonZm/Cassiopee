def loadIcicle():
	icicles=[]
	line=input().strip().split()
	N,L=map(int,line)
	while len(icicles)<N: icicles.append(int(input()))
	return icicles,N,L

def calcDiff(icicles,N):
	diff2=[0]*N
	for i in range(N):
		right=icicles[i+1]-icicles[i] if i<N-1 else -icicles[i]
		left=icicles[i]-icicles[i-1] if i>0 else icicles[i]
		right=1 if right>0 else -1
		left=1 if left>0 else -1
		diff2[i]=(-1 if right-left<0 else 1) if right-left!=0 else 0
	return diff2

icicles,N,L=loadIcicle()
diff2=calcDiff(icicles,N)
time=[-1]*N
peaks=[i for i,d in enumerate(diff2) if d==-1]
for p in peaks:
	time[p]=L - icicles[p]
	left,right=p,p
	doneL,doneR=False,False
	while not(doneL and doneR):
		left-=1
		if left<0:
			doneL=True
		else:
			if time[left]==-1:
				time[left]=(L-icicles[left])+time[left+1]
			else:
				rght=max(time[left-1] if left-1>=0 else 0, time[left+1])
				time[left]=(L-icicles[left])+rght
			if diff2[left]==1: doneL=True
		right+=1
		if right>=N:
			doneR=True
		else:
			if time[right]==-1:
				time[right]=(L-icicles[right])+time[right-1]
			else:
				lft=max(time[right-1], time[right+1] if right+1<N else 0)
				time[right]=(L-icicles[right])+lft
			if diff2[right]==1: doneR=True
print(max(time))