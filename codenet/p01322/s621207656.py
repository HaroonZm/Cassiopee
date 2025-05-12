while True:
    n, m = map(int, input().split())
    if n == 0:
        break

    N, M = zip(*[[x.strip("*") if i == 0 else int(x) for i, x in enumerate(input().split())] for _ in range(n)])

    print(sum([M[i] for b in [input() for _ in range(m)] for i, x in enumerate(N) if b.endswith(x)]))