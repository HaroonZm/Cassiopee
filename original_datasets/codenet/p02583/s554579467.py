from itertools import combinations
n = int(input())
l = list(map(int,input().split()))
c = combinations(l,3)
k=0
for (a,b,c) in c:
	if a+b>c and b+c>a and c+a>b and a!=b and b!=c and a!=c:
		k+=1
print(k)