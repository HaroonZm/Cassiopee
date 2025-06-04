import sys
import math
import heapq

def main():
    def distance(x1, y1, x2, y2):
        if y1 == y2:
            return abs(x1 - x2)
        return math.hypot(x1 - x2, y1 - y2)

    while True:
        try:
            n = int(sys.stdin.readline())
        except:
            break
        if n == 0:
            break
        points = []
        for _ in range(n):
            x, y = map(int, sys.stdin.readline().split())
            points.append((x, y))
        ys = set()
        for x, y in points:
            ys.add(y)
        new_points = points[:]
        for i in range(n-1):
            x0, y0 = points[i]
            x1, y1 = points[i+1]
            if y0 != y1:
                for y in ys:
                    if (y0 < y < y1) or (y1 < y < y0):
                        x = (x1 - x0)/(y1 - y0)*(y - y0) + x0
                        new_points.append((x, y))
        new_points.sort()
        L = len(new_points)
        INF = 1 << 60
        heap = []
        heapq.heappush(heap, (0, 0, L-1))
        dist = {}
        dist[(0, L-1)] = 0
        directions = [(1, -1), (1, 0), (0, -1), (-1, 0), (0, 1), (1, 1), (-1, -1), (-1, 1)]
        found = False
        while heap:
            cost, a, b = heapq.heappop(heap)
            if dist.get((a, b), INF) < cost:
                continue
            if a == b:
                print("%.16f" % cost)
                found = True
                break
            ax, ay = new_points[a]
            bx, by = new_points[b]
            for da, db in directions:
                na = a + da
                nb = b + db
                if not (0 <= na <= nb < L):
                    continue
                cx, cy = new_points[na]
                dx, dy = new_points[nb]
                if cy != dy:
                    continue
                ncost = cost + distance(ax, ay, cx, cy) + distance(bx, by, dx, dy)
                key = (na, nb)
                if dist.get(key, INF) > ncost:
                    dist[key] = ncost
                    heapq.heappush(heap, (ncost, na, nb))
        if not found:
            print(-1)

main()