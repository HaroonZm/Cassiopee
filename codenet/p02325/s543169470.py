import math
from typing import List, Tuple

def dist(p1: Tuple[int, int], p2: Tuple[int, int]) -> float:
    return math.sqrt((p1[0] - p2[0]) ** 2 + (p1[1] - p2[1]) ** 2)

if __name__ == "__main__":
    N = int(input())
    points: List[Tuple[int, int]] = [(0, 0)] * N
    for idx in range(N):
        x, y = map(lambda x: int(x), input().split())
        points[idx] = (x, y)

    table1 = [float('inf')] * N
    table2 = [float('inf')] * N
    table1[0] = table2[0] = dist(points[0], points[1])

    for i in range(2, N):
        d1 = d2 = float('inf')
        for j in range(i - 1):
            d = dist(points[i], points[j])
            d1 = min(d1, table2[j] + d)
            d2 = min(d2, table1[j] + d)
        table1[i - 1] = d1
        table2[i - 1] = d2
        d = dist(points[i - 1], points[i])
        for j in range(i - 1):
            table1[j] += d
            table2[j] += d

    ans = min(min(d1, d2) + dist(points[i], points[N - 1])
              for i, (d1, d2) in enumerate(zip(table1, table2)))
    print(ans)