INF = 10**20
MAX_INT = 10**6
a = [INF] * MAX_INT
b = [INF] * MAX_INT
a[0],b[0] = 0,0
for i in range(1, 200):
    t = i*(i+1)*(i+2)//6
    mm = min(t*5, MAX_INT)
    for j in range(t, mm):
        if a[j] > a[j-t]+1:
            a[j] = a[j-t]+1
    if t%2==0:
        continue
    for j in range(t, MAX_INT):
        if b[j] > b[j-t]+1:
            b[j] = b[j-t]+1
while True:
    N = int(input())
    if N==0:
        exit()
    print(a[N], b[N])