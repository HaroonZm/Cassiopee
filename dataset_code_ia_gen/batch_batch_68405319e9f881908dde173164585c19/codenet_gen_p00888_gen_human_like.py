import sys
import math
from heapq import heappush, heappop

def distance(p1, p2):
    return math.hypot(p1[0] - p2[0], p1[1] - p2[1])

def main():
    input = sys.stdin.read().strip().split()
    idx = 0
    while True:
        if idx >= len(input):
            break
        N = int(input[idx])
        idx += 1
        if N == 0:
            break
        points = []
        for _ in range(N):
            x = float(input[idx])
            y = float(input[idx + 1])
            idx += 2
            points.append((x, y))

        # Precompute segments lengths
        seg_len = [distance(points[i], points[i+1]) for i in range(N-1)]

        # States: positions of the two climbers on the route:
        # i, j represent positions at points i and j (indices)
        # climber 1 moves forward or backward along route points
        # climber 2 moves forward or backward along route points from the other end
        # but i always in [0..N-1], j in [0..N-1]
        # Both climbers must maintain the same altitude, i.e. y_i == y_j.

        # Use Dijkstra to find minimum sum length meeting point

        # Precompute altitudes for quick check
        altitudes = [p[1] for p in points]

        # Only allow states where altitudes[i] == altitudes[j]
        # The problem guarantees start and end alt have zero and no point lower than 0 (start altitude)
        # So climbers start at i=0 and j=N-1

        INF = float('inf')
        dist = [[INF]*N for _ in range(N)]
        dist[0][N-1] = 0
        heap = [(0, 0, N-1)]

        # moves: climber1 can go to i-1 or i+1 if valid
        # climber2 can go to j-1 or j+1 if valid
        # but need to maintain altitudes equal: altitudes[new_i] == altitudes[new_j]

        while heap:
            d, i, j = heappop(heap)
            if i == j:
                # Met
                print(f"{d:.10f}")
                break
            if dist[i][j] < d:
                continue

            # possible moves for climber 1
            c1_positions = []
            if i > 0:
                c1_positions.append(i-1)
            if i < N-1:
                c1_positions.append(i+1)

            # possible moves for climber 2
            c2_positions = []
            if j > 0:
                c2_positions.append(j-1)
            if j < N-1:
                c2_positions.append(j+1)

            # try all moves combinations moving simultaneously
            for ni in c1_positions:
                for nj in c2_positions:
                    if altitudes[ni] == altitudes[nj]:
                        # compute additional distance moved by both
                        # distance for climber 1
                        d_i = seg_len[min(i, ni)]  # segment between i and ni
                        d_j = seg_len[min(j, nj)]
                        nd = d + d_i + d_j
                        if dist[ni][nj] > nd:
                            dist[ni][nj] = nd
                            heappush(heap, (nd, ni, nj))
        else:
            # theoretically problem guarantees a solution
            print("0.0")

if __name__ == "__main__":
    main()