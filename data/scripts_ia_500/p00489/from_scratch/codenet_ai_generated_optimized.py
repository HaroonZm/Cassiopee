N=int(input())
points=[0]*N
for _ in range(N*(N-1)//2):
    A,B,C,D=map(int,input().split())
    if C>D:
        points[A-1]+=3
    elif C<D:
        points[B-1]+=3
    else:
        points[A-1]+=1
        points[B-1]+=1
sorted_points=sorted([(p,i) for i,p in enumerate(points)],reverse=True)
ranks=[0]*N
rank=1
for i,(p,idx) in enumerate(sorted_points):
    if i>0 and p!=sorted_points[i-1][0]:
        rank=i+1
    ranks[idx]=rank
print(*ranks,sep='\n')