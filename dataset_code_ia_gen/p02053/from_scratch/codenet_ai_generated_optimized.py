H,W=map(int,input().split())
positions=[(i,j) for i in range(H) for j,c in enumerate(input()) if c=='B']
min_i=min(p[0] for p in positions)
max_i=max(p[0] for p in positions)
min_j=min(p[1] for p in positions)
max_j=max(p[1] for p in positions)
print((max_i - min_i) + (max_j - min_j))