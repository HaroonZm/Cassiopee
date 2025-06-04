UTF8pattern = [['0xxxxxxx'],
    ['110yyyyx','10xxxxxx'],
    ['1110yyyy','10yxxxxx','10xxxxxx'],
    ['11110yyy','10yyxxxx', '10xxxxxx', '10xxxxxx']
    ]

def func(linelist, pattern):
    mother = UTF8pattern[pattern-1]
    ret = 1
    rety = 1
    y_hasone = 0
    y_allzero = 1
    for i in range(pattern):
        for j in range(8):
            if (mother[i][j]=='0' or mother[i][j]=='1') and linelist[i][j]!='x' and mother[i][j]!=linelist[i][j]:
                return 0
            if mother[i][j]=='x' and linelist[i][j]=='x':
                ret *= 2
            if mother[i][j]=='y':
                if linelist[i][j]=='1':
                    y_hasone = 1
                    y_allzero = 0
                elif linelist[i][j]=='x':
                    y_allzero = 0
                    rety *= 2
    if pattern >= 2:
        if y_allzero:
            return 0
        elif not y_hasone:
            rety -= 1
        ret *= rety
    return ret

while 1:
    N = int(raw_input())
    if N == 0:
        break
    L = []
    for n in range(N):
        L.append(raw_input())
    A = [[0 for x in range(4)] for y in range(N)]
    for n in range(N):
        for p in range(4):
            if n + p < N:
                A[n][p] = func(L[n:n+p+1], p+1)
    B = [0 for y in range(N+1)]
    B[0] = 1
    for n in range(N+1):
        for p in range(4):
            if n - p > 0:
                B[n] += B[n-p-1]*A[n-p-1][p]
    print B[-1]%1000000