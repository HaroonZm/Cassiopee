n=int(input())
for _ in range(n):
    grid=[input().split() for __ in range(9)]
    row_counts=[{str(d):0 for d in range(1,10)} for __ in range(9)]
    col_counts=[{str(d):0 for d in range(1,10)} for __ in range(9)]
    box_counts=[{str(d):0 for d in range(1,10)} for __ in range(9)]
    # Count occurrences
    for i in range(9):
        for j in range(9):
            num=grid[i][j]
            row_counts[i][num]+=1
            col_counts[j][num]+=1
            box_counts[(i//3)*3+(j//3)][num]+=1
    # Check duplicates
    mark=[[False]*9 for __ in range(9)]
    for i in range(9):
        for j in range(9):
            num=grid[i][j]
            if row_counts[i][num]>1 or col_counts[j][num]>1 or box_counts[(i//3)*3+(j//3)][num]>1:
                mark[i][j]=True
    for i in range(9):
        line=""
        for j in range(9):
            line+=('*' if mark[i][j] else ' ') + grid[i][j]
        print(line)
    print()