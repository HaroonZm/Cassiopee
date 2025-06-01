n=int(input())
p=list(map(int,input().split()))
p.sort(reverse=True)
score=0
for i in range(1,n+1):
    if p[i-1]>=i:
        score=i
print(score)