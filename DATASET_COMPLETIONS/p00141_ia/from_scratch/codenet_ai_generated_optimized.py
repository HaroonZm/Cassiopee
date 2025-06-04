d=int(input())
for _ in range(d):
    n=int(input())
    mat=[[' ']*n for __ in range(n)]
    top,bottom,left,right=0,n-1,0,n-1
    c='#'
    while left<=right and top<=bottom:
        for i in range(left,right+1):
            mat[bottom][i]=c
        bottom-=1
        for i in range(bottom,top-1,-1):
            mat[i][right]=c
        right-=1
        if top<=bottom:
            for i in range(right,left-1,-1):
                mat[top][i]=c
            top+=1
        if left<=right:
            for i in range(top,bottom+1):
                mat[i][left]=c
            left+=1
        c=' ' if c=='#' else '#'
    for i in range(n-1,-1,-1):
        print(''.join(mat[i]))
    print()