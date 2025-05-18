from bisect import bisect_right
N,M=map(int,input().split())
PY=[]
record=[[] for i in range(N+1)]
for i in range(M):
    P,Y=map(int,input().split())
    PY.append([P,Y])
    record[P].append(Y)
for i in range(1,N+1):
    record[i].sort()
for i in range(M):
    p,y=PY[i][0],PY[i][1]
    order=bisect_right(record[p],y)
    print(str(p).zfill(6)+str(order).zfill(6))