import queue, math
while True:
    n = int(input())
    if n == 0: break
    p = [[float(x) for x in input().split()] for _ in range(n)]
    g = [i for i in range(n)]

    def root(x):
        if x == g[x]: return x
        g[x] = root(g[x])
        return g[x]

    q = queue.PriorityQueue()
    cnt_g = n
    ans = 0.0
    for i in range(n-1):
        for j in range(i,n):
            d = math.sqrt((p[i][0]-p[j][0])**2 + (p[i][1]-p[j][1])**2 + (p[i][2]-p[j][2])**2)
            if d <= p[i][3] + p[j][3] :
                if root(i) != root(j):
                    g[root(i)] = root(j)
                    cnt_g -= 1
            else:
                q.put((d-p[i][3]-p[j][3],i,j))

    while not q.empty():
        if cnt_g <= 1 : break
        d, i, j = q.get()
        if root(i) != root(j):
            g[root(i)] = root(j)
            cnt_g-= 1
            ans += d

    print ('{:.3f}'.format(ans))