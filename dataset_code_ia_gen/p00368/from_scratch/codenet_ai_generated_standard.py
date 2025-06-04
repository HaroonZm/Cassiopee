W,H=map(int,input().split())
grid=[list(map(int,input().split())) for _ in range(H)]
def can_form_checkered(grid,W,H):
    row0=grid[0]
    row1=[(x^1) for x in row0]
    for r in range(H):
        if grid[r]!=row0 and grid[r]!=row1:
            return False
    col0=[grid[i][0] for i in range(H)]
    col1=[(x^1) for x in col0]
    for c in range(W):
        col=[grid[r][c] for r in range(H)]
        if col!=col0 and col!=col1:
            return False
    if row0==row1 or col0==col1:
        return False
    if row0.count(row0[0])!=len(row0) or col0.count(col0[0])!=len(col0):
        return False
    return sum(row0)==W//2 or sum(row0)==(W+1)//2 and sum(col0)==H//2 or sum(col0)==(H+1)//2
print("yes" if can_form_checkered(grid,W,H) else "no")