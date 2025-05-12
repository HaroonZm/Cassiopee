n,k = (int(i) for i in input().split())
x = [[4,2,0,9,7]]+[[0 for i in range(5)] for i in range(10)]
for i in range(1,11):
	for j in range(5):
		x[i][j] = (x[i-1][j]+8)%11
ans,m = ((n-2)//11)*5,(n-2)%11
for i in range(m): ans+=x[i].count(k)
print(ans)