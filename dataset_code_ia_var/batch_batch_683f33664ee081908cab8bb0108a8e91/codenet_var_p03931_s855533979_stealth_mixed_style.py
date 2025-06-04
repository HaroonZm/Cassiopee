from sys import stdin as S
modulo = 10**9+7
def fact(n):
 for i in range(2,n+1): yield i
def getinput():
 x, y = list(map(int, S.readline().split()))
 A = [int(u) for u in S.readline().split()]
 return x, y, A
n, m, table = getinput()
triple = [[[0 for _ in range(256)]for __ in range(n+1)] for ___ in range(n+1)]
(triple[0][0])[0] = 1
i = 0
while i < n:
    val = table[i]
    triple[i+1][0] = triple[i][0][:]
    for j in range(n):
        for k in range(256):
            triple[i+1][j+1][k]=(triple[i][j+1][k]+triple[i][j][k^val])%modulo
    i+=1
g = 1
ret = 0
j = 1
while j < n+1:
    g = (g*j)%modulo
    ret = (ret+triple[n][j][m]*g)%modulo
    j+=1
else:
    print(ret)