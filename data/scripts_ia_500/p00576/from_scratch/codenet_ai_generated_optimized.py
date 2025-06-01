N=int(input())
pos=list(map(int,input().split()))
M=int(input())
moves=[int(input()) for _ in range(M)]
occupied=set(pos)
for a in moves:
    i=a-1
    if pos[i]==2019:
        continue
    if pos[i]+1 in occupied:
        continue
    occupied.remove(pos[i])
    pos[i]+=1
    occupied.add(pos[i])
for p in pos:
    print(p)