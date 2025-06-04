d=int(input())
for _ in range(d):
    n=int(input())
    grid=[[' ']*n for _ in range(n)]
    top,bottom,left,right=0,n-1,0,n-1
    while left<=right and top<=bottom:
        for c in range(left,right+1):
            grid[bottom][c]='#'
        bottom-=1
        for r in range(bottom,top-1,-1):
            grid[r][right]='#'
        right-=1
        if top<=bottom:
            for c in range(right,left-1,-1):
                grid[top][c]='#'
            top+=1
        if left<=right:
            for r in range(top,bottom+1):
                grid[r][left]='#'
            left+=1
    for row in grid:
        print(''.join(row))
    print()