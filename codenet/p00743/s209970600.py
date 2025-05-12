from heapq import heappush, heappop

def main():
    while True:
        n, m = map(int, input().split())
        if n == 0:
            break
        s, g = map(int, input().split())
        s -= 1
        g -= 1
        edges = [[] for _ in range(n)]
        for _ in range(m):
            x, y, d, c = map(int, input().split())
            x -= 1
            y -= 1
            edges[x].append((y, d, c))
            edges[y].append((x, d, c))

        que = []
        heappush(que, (0, 1, s, None))
        dic = {}
        dic[(1, None, s, None)] = 0
        INF = 10 ** 20
        ans = INF
        while que:
            score, speed, node, pre_node= heappop(que)
            if score >= ans:break
            for to, dist, limit in edges[node]:
                if to == pre_node or speed > limit:continue
                new_score = score + dist / speed
                if speed == 1 and to == g and ans > new_score:ans = new_score
                for new_speed in (speed - 1, speed, speed + 1):
                    if new_speed <= 0:continue
                    if (new_speed, to, node) not in dic or dic[(new_speed, to, node)] > new_score:
                        dic[(new_speed, to, node)] = new_score
                        heappush(que, (new_score, new_speed, to, node))
        if ans == INF:
            print("unreachable")
        else:
            print(ans)

main()