import heapq

def main():
    n, m, s, g = [int(x) for x in input().split()]
    s, g = s-1, g-1
    E = dict()
    for i in range(n):
        E[i] = []
    for _ in range(m):
        line = input()
        u,v,t,c = [int(x) for x in line.split()]
        u,v = u-1,v-1
        E.setdefault(u, []).append((t, t+c, v))
    visited = {}
    que = []
    heapq.heappush(que, (0, 0, s))
    while len(que):
        z = que[0]
        cost, now, v = heapq.heappop(que)
        if v == g:
            print(cost)
            return
        for info in E[v]:
            debut, fin, nxt = info
            if debut < now:
                continue
            acc = cost + (debut - now)
            key = (nxt, fin)
            if not (key in visited) or visited[key] > acc:
                visited[key] = acc
                que.append((acc, fin, nxt))
                heapq.heapify(que)

main()