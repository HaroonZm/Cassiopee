from typing import Tuple, List
from heapq import heappush, heappop

def max_value(max_weight: int, items: List[Tuple[int, int]]) -> float:
    def _cost(weight: int, value: int, i: int) -> Tuple[int, float]:
        # Use value as negative cost
        for j in range(i, n):
            v, w = items[j]
            if (weight + w > max_weight):
                return (-value, -value - (v / w) * (max_weight - weight))
            weight += w
            value += v
        return (-value, -value * 1.0)

    n = len(items)
    items.sort(key=lambda x: x[1], reverse=True)
    items.sort(key=lambda x: x[0] / x[1], reverse=True)
    u, c = _cost(0, 0, 0)
    heap = [(c, u, 0, 0, 0)]
    maxcost = u
    while heap:
        cost, upper, weight, value, i = heappop(heap)
        if (cost > maxcost):
            break
        if (i < n):
            v, w = items[i]
            if (weight + w <= max_weight):
                heappush(heap, (cost, upper, weight + w, value + v, i + 1))
            u, c = _cost(weight, value, i + 1)
            if (c < maxcost):
                if (u < maxcost):
                    maxcost = u
                heappush(heap, (c, u, weight, value, i + 1))

    return -maxcost

if __name__ == '__main__':
    N, W = map(lambda x: int(x), input().split())
    items: List[Tuple[int, int]] = []

    for _ in range(N):
        v, w, m = map(lambda x: int(x), input().split())
        for i in range(m.bit_length() - 1):
            h = 2 ** i
            m -= h
            items.append((v * h, w * h))
        if m > 0:
            items.append((v * m, w * m))

    print(max_value(W, items))