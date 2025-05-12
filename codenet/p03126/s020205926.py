N,M = map(int, input().split())
like=[]
cnt=0
for i in range(N):
	like.append(list(map(int, input().split()))[1:])
for j in range(1,M+1):
	if all ([j in x for x in like]):
		cnt += 1
print(cnt)