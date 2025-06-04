INF = 10 ** 20

m_n = input().split()
m = int(m_n[0])
n = int(m_n[1])

L = []
for idx in range(m):
    L.append(int(input()))
L = sorted(L, key=lambda x: -x)

def accumulate(_lst):
    a = 0
    res = [0]
    for v in _lst:
        a += v
        res.append(a)
    return res

S = accumulate(L)

def get_input_list(times):
    r1 = []
    r2 = []
    for ind in range(times):
        a, b = input().split()
        r1.append(int(a))
        r2.append(int(b))
    return r1, r2

cList, eList = get_input_list(n)

array = [[INF for _ in range(m+1)] for __ in range(n)]
for x in range(n):
    array[x][0] = 0

for ix in range(n):
    c, e = cList[ix], eList[ix]
    rng = list(range(m, 0, -1))
    for iy in rng:
        if iy >= c:
            left = 0
            if ix-1 >= 0:
                left = array[ix-1][iy-c]
            else:
                left = INF
            array[ix][iy] = min(array[ix-1][iy], left + e)
        else:
            if iy + 1 <= m:
                array[ix][iy] = min(array[ix-1][iy], array[ix][iy+1])
            else:
                array[ix][iy] = min(array[ix-1][iy], e)

MM = [S[i] - array[n-1][i] for i in range(m+1)]
ans = -float('inf')
for item in MM:
    if item > ans:
        ans = item
print(ans)