N=int(input())
positions=list(map(int,input().split()))
M=int(input())
moves=[int(input()) for _ in range(M)]
pos_by_piece=positions
occupied=set(positions)
for a in moves:
    idx=a-1
    if pos_by_piece[idx]==2019:
        continue
    if (pos_by_piece[idx]+1) in occupied:
        continue
    occupied.remove(pos_by_piece[idx])
    pos_by_piece[idx]+=1
    occupied.add(pos_by_piece[idx])
for p in pos_by_piece:
    print(p)