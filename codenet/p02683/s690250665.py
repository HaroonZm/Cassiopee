n,m,x = list(map(int,input().split()))
c = [[] for i in range(n)]

for i in range(n):
    c[i] = list(map(int,input().split()))

check = [0]*n

def dekiru(ls):
    hantei = [0]*m
    for i in range(n):
        if check[i] == 1:
            for j in range(m):
                hantei[j] += c[i][j+1]
    for i in range(m):
        if hantei[i] < x:
            return False
    return True

ans = 10000000000000000000000

def solv(idx):
    global ans
    if idx == n:
        kane = 0
        for i in range(n):
            if check[i] == 1:
                kane += c[i][0]
        if dekiru(check):
            ans = min(ans,kane)
        return

    check[idx] = 0
    solv(idx+1)
    check[idx] = 1
    solv(idx+1)

solv(0)
print(ans if ans != 10000000000000000000000 else -1)