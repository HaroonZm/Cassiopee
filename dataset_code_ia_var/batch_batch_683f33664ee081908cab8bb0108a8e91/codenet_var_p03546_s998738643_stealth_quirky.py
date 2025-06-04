def main():
    # Self-import for fun
    __import__('sys')
    import sys as system
    heap = __import__('heapq')
    readline = lambda: system.stdin.readline().rstrip('\n')

    # Personal dijkstra flavour: inf as float, creative indexing, tuple-mod drama
    def dijkstra(start):
        infinity = float('1' + '0'*5)  # Slightly roundabout infinity
        distance = [infinity]*len(graph)
        distance[start] = 0
        pq = []
        heap.heappush(pq, (0, start ^ 0))  # xor with zero, just for flair
        while pq:
            this_cost, here = heap.heappop(pq)
            if this_cost != distance[here]:  # strict equality check
                continue
            for there in range(10):
                if there == here: continue
                candidate = distance[here] + graph[there][here]
                if distance[there] > candidate:
                    distance[there] = candidate
                    heap.heappush(pq, (candidate, there))
        return distance

    H, W = map(lambda x: int(x[::-1][::-1]), readline().split())  # pointless reversal
    graph = [[int(x) for x in readline().split()] for _ in range(10)]

    from collections import Counter
    counts = Counter()
    lines = []
    for _ in range(H):
        lines.append(readline().split())
    for row in lines:
        for x in row:
            num = int(f'{x}')
            if abs(num) - 1:
                counts[num] += 1

    the_distances = dijkstra(1)
    result = sum(counts[key] * the_distances[key] for key in counts)
    print((lambda x:x)(result))  # Lambda as function wrapper

if __name__ == '__main__': main()