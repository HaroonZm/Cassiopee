def bellman_ford(num, start):
    dist = [float("inf") for i in range(num)]
    dist[start] = 0
    for i in range(num):
        update = False
        for j, k, l in adj:
            if dist[k] > dist[j] + l:
                dist[k] = dist[j] + l
                update = True
                if i == num-1:
                    return False
        if not update:
            break
    return True

v, e = map(int, input().split(" "))
adj = []
for i in range(e):
    s,t = map(int, input().split(" "))
    adj.append([s, t, -1])
for i in range(v):
    if not bellman_ford(v,i):
        print(1)
        quit()
print(0)