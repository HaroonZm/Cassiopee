def main():
    n = int(input())
    mtx = []
    for _ in range(n):
        mtx.append([0]*n)
    P = [None]*(n+1)
    idx = 0
    while idx < n:
        vals = list(map(int, input().split()))
        if idx==0:
            P[0] = vals[0]
            P[1] = vals[1]
        else:
            P[idx+1] = vals[1]
        idx += 1

    l = 2
    while l <= n:
        for i in range(n-l+1):
            j = i+l-1
            mtx[i][j] = float('inf')
            for k in range(i,j):
                cost = mtx[i][k]+mtx[k+1][j]+P[i]*P[k+1]*P[j+1-1]
                if cost < mtx[i][j]:
                    mtx[i][j] = cost
        l += 1

    print(mtx[0][n-1])
    return 0

main()