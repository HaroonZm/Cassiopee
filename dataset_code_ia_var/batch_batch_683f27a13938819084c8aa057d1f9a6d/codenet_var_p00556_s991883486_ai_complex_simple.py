def main():
    from functools import reduce
    from operator import or_, add
    import itertools

    N, M = map(int, input().split())
    a = list(map(lambda _: int(input())-1, range(N)))

    S = list(map(lambda _: [0]*N, range(20)))
    C = list(map(lambda _: 0, range(20)))
    ans_bit = reduce(or_, (1<<x for x in a), 0)

    def enumerate_prefix_sums():
        for i, val in enumerate(a):
            C[val] += 1
            S[val][i] = 1
        cumsum = lambda arr: list(itertools.accumulate(arr))
        for j in range(20):
            S[j] = cumsum(S[j])

    enumerate_prefix_sums()

    inf = 10**9
    size = 1 << 20
    D = [inf]*size
    D[0] = 0

    for bits in filter(lambda x: D[x]!=inf, range(size)):
        v = reduce(add, (C[u] for u in range(20) if (bits>>u)&1), 0)
        for u in filter(lambda y: C[y] and not ((bits>>y)&1), range(20)):
            w = v + C[u]
            not_move = S[u][w-1] - (S[u][v-1] if v else 0)
            move = C[u] - not_move
            nxt = bits | (1<<u)
            D[nxt] = min(D[nxt], D[bits]+move)

    print(D[ans_bit])

if __name__ == "__main__":
    main()