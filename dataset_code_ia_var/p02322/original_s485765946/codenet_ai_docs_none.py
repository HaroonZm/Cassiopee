from heapq import heappush, heappop

def max_value(t, xs):
    def _cost(weight, value, i):
        for j in range(i, n):
            v, w = xs[j]
            if weight + w > t:
                return (-value, -value - (v/w)*(t-weight))
            weight += w
            value += v
        return (-value, -value*1.0)

    n = len(xs)
    xs.sort(key=lambda x: x[1], reverse=True)
    xs.sort(key=lambda x: x[0]/x[1], reverse=True)
    u, c = _cost(0, 0, 0)
    heap = [(c, u, 0, 0, 0)]
    maxcost = u
    while heap:
        cost, upper, weight, value, i = heappop(heap)
        if cost > maxcost:
            break
        if i < n:
            v, w = xs[i]
            if weight+w <= t:
                heappush(heap, (cost, upper, weight+w, value+v, i+1))
            u, c = _cost(weight, value, i+1)
            if c < maxcost:
                if u < maxcost:
                    maxcost = u
                heappush(heap, (c, u, weight, value, i+1))
    return -maxcost

def run():
    n, t = [int(i) for i in input().split()]
    xs = []
    for _ in range(n):
        v, w, m = [int(i) for i in input().split()]
        for i in range(m.bit_length()-1):
            h = 2**i
            m -= h
            xs.append((v*h, w*h))
        if m > 0:
            xs.append((v*m, w*m))
    print(max_value(t, xs))

if __name__ == '__main__':
    run()