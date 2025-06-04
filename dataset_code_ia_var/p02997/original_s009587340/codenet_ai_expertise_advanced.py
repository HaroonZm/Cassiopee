from sys import exit

def main():
    N, K = map(int, input().split())
    max_non_bridge = (N - 1) * (N - 2) // 2

    if max_non_bridge < K:
        print(-1)
        return

    edges = [[i] for i in range(1, N)]

    ef, et = 1, 2
    added = 0
    while added < max_non_bridge - K:
        if et == ef:
            et += 1
        if et >= N:
            ef += 1
            et = ef + 1
            continue
        edges[ef].append(et)
        added += 1
        et += 1

    total_edges = sum(map(len, edges))
    print(total_edges)
    for u, lst in enumerate(edges):
        for v in lst:
            print(u + 1, v + 1)

if __name__ == "__main__":
    main()