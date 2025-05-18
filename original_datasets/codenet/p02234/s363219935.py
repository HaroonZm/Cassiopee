def main():
    n = int(raw_input())
    m = [ [0] * n for _ in xrange(n)]
    p = [ 0 for _ in xrange(n+1)]
    for i in xrange(n):
        a = map(int, raw_input().split())
        if i == 0:
            p[0] = a[0]
            p[1] = a[1]
        else:
            p[i+1] = a[1]

    for l in xrange(2,n+1):
        for i in xrange(0,n-l+1):
            j = i + l -1
            m[i][j] = float('inf')
            for k in xrange(i,j):
                m[i][j] = min(m[i][j], m[i][k]+m[k+1][j] + p[i-1]*p[k]*p[j])
    
    print m[0][n-1]
    return 0

main()