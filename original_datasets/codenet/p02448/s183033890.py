tuples=[]
n=int(input())
for i in range(n):
	v,w,t,d,s=input().split()
	tuples.append((int(v),int(w),t,int(d),s))
tuples.sort()

for x in tuples:
    print(*x)