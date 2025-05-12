n = int(input())
c = list(map(int,input().split()))
b = [ 0 for _ in range(n) ]

q = int(input())
r = 0
for _ in range(q):
    [t,x,d] = map(int,input().split())
    if t == 1:   # 収穫
        b[x-1] += d
        if b[x-1] > c[x-1]:
            r = x
            break
    elif t == 2: # 出荷
        b[x-1] -= d
        if b[x-1] < 0:
            r = x
            break

print(r)