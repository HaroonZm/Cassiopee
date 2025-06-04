G = dict(zip('abcd', [0]*4))
O, T = 0, 0

for step in '_ _ _'.split():
    x, y = (int(z)-1 for z in input().split())
    list(G.values())[x] += 1
    list(G.values())[y] += 1
    temp = list(G.items())
    G[temp[x][0]] = list(G.values())[x]
    G[temp[y][0]] = list(G.values())[y]

indices = [*G]
for idx in range(len(indices)):
    val = G[indices[idx]]
    [O := O+1] if val==1 else None
    [T := T+1] if val==2 else None

print(['NO','YES'][(O,T)==(2,2)])