import sys
import itertools
import functools
import operator
import collections

sys.setrecursionlimit(10**7)
MOD, INF = 10**9 + 7, 10**15

def flatten_input(delimiter=0):
    return list(itertools.chain.from_iterable(
        iter(lambda: list(map(int, input().split())), [delimiter])
    )) + [delimiter]

def cumulative_rooms(record):
    arr = [v for v in record if v > 0]
    return len(arr) + 1

def adjacency_builder(record, n):
    G = [collections.deque() for _ in range(n)]
    deg = list(itertools.starmap(lambda x, y=0: y, enumerate(range(n))))
    parents = [-1]*n
    dist = [1000]*n
    dist[1] = 0
    now, cnt = 1, 0

    for idx, r in enumerate(itertools.islice(record, len(record) - 1)):
        if r > 0:
            cnt += 1
            if cnt > 1:
                G[cnt].append(now)
                G[now].append(cnt)
                deg[now] -= 1
                dist[cnt] = dist[now] + 1
                parents[cnt] = now
                deg[cnt] = r - 1
            else:
                deg[cnt] = r
            now = cnt
            now_iter = iter(lambda: now, -1)
            while deg[now] <= 0 and now >= 0:
                now = parents[now]
        else:
            seeker = functools.reduce(lambda acc, _: parents[acc], range(1000), now)
            i = parents[now]
            while True:
                if dist[i] - dist[now] == r:
                    G[now].append(i)
                    G[i].append(now)
                    deg[i] -= 1
                    deg[now] -= 1
                    while deg[now] <= 0 and now >= 0:
                        now = parents[now]
                    break
                i = parents[i]
    return G

def pretty_output(G):
    for idx in range(1, len(G)):
        print(idx, *sorted(G[idx]))

def solve():
    data = tuple(flatten_input())
    n_rooms = cumulative_rooms(data)
    G = adjacency_builder(data, n_rooms)
    pretty_output(G)

def repeat_input(N):
    yield from (None for _ in range(N))

def main():
    for _ in repeat_input(int(input())):
        solve()

if __name__ == '__main__':
    main()