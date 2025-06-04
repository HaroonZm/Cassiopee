import sys
from itertools import product
from functools import lru_cache

input = sys.stdin.readline
INF = 10**13

def main():
    N = int(input())
    T = [tuple(map(int, input().split())) for _ in range(N)]

    # Precompute all X/Y axis distances for each bitmask of selected villages
    X_dist = [[0] * N for _ in range(1 << N)]
    Y_dist = [[0] * N for _ in range(1 << N)]

    x0, y0 = 0, 0

    for bit in range(1 << N):
        xs = [x0]
        ys = [y0]
        for i in range(N):
            if bit & (1 << i):
                xs.append(T[i][0])
                ys.append(T[i][1])
        for i, (x, y, p) in enumerate(T):
            X_dist[bit][i] = p * min(abs(x_sel - x) for x_sel in xs)
            Y_dist[bit][i] = p * min(abs(y_sel - y) for y_sel in ys)

    answer = [INF] * (N + 1)

    for bit in range(1 << N):
        cnt = bin(bit).count('1')
        sub = bit
        # enumerate all submasks
        while True:
            sub_X = sub         # sub_X is the set of villages assigned X-axis
            sub_Y = bit ^ sub   # sub_Y is the set assigned Y-axis (disjont from sub_X)
            cost = 0
            for k in range(N):
                # if village k not built yet, compute min cost for it
                if not (bit >> k) & 1:
                    cost += min(X_dist[sub_X][k], Y_dist[sub_Y][k])
            answer[cnt] = min(answer[cnt], cost)
            if sub == 0:
                break
            sub = (sub - 1) & bit

    print('\n'.join(map(str, answer)))

if __name__ == '__main__':
    main()