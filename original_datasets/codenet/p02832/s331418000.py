n=int(input())
*a,=map(int,input().split())
l=1
cnt=0
if 1 in a:
	for i in a:
		if i==l:
			cnt+=1
			l+=1
	print(n-cnt)
else:
	print(-1)