N=int(input())
a=[float(input()) for _ in range(N)]
points=[0]*N
for i in range(N):
    for j in range(i+1,N):
        if a[i]>a[j]:
            points[i]+=3
        elif a[i]<a[j]:
            points[j]+=3
        else:
            points[i]+=1
            points[j]+=1
print(*points, sep='\n')