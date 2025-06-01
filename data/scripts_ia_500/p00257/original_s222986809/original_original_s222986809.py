import queue

while True:
    m = int(input())
    if m == 0:
        break
    n = int(input())
    d = [0]*(n+2)
    for i in range(1,n+1):
        d[i] = int(input())
    visited = [False]*(n+2)
    visited[0] = True
    ok = [False]*(n+2)
    ok[n+1] = True
    rev = [[] for _ in range(n+2)]
    
    que = queue.LifoQueue()
    que.put(0)
    while not que.empty():
        i = que.get()
        for j in range(1,m+1):
            if i+j > n+1:
                break
            k = min(max(i+j+d[i+j], 0), n+1)
            rev[k].append(i)
            if not visited[k]:
                que.put(k)
                visited[k] = True

    que.put(n+1)
    while not que.empty():
        i = que.get()
        for j in rev[i]:
            if not ok[j]:
                ok[j] = True
                que.put(j)

    ans = 'OK'
    if not visited[n+1]:
        ans = 'NG'
    for i in range(n+1):
        if visited[i] and (not ok[i]):
            ans = 'NG'
    print(ans)