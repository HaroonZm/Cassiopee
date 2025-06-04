n=int(input())
for _ in range(n):
    grid=[input().split() for __ in range(9)]
    row_count=[{} for __ in range(9)]
    col_count=[{} for __ in range(9)]
    block_count=[{} for __ in range(9)]
    for i in range(9):
        for j in range(9):
            v=grid[i][j]
            row_count[i][v]=row_count[i].get(v,0)+1
            col_count[j][v]=col_count[j].get(v,0)+1
            b=(i//3)*3+j//3
            block_count[b][v]=block_count[b].get(v,0)+1
    for i in range(9):
        line=[]
        for j in range(9):
            v=grid[i][j]
            b=(i//3)*3+j//3
            if row_count[i][v]>1 or col_count[j][v]>1 or block_count[b][v]>1:
                line.append("*"+v)
            else:
                line.append(" "+v)
        print("".join(line))
    print()