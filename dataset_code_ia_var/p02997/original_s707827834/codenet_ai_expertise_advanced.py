from sys import stdout

def main():
    import sys

    N, K = map(int, sys.stdin.readline().split())
    max_extra = (N-1)*(N-2)//2
    if K > max_extra:
        print(-1)
        return

    edges = [(1, i) for i in range(2, N+1)]
    cnt = max_extra

    def edge_pairs():
        for i in range(2, N):
            for j in range(i+1, N+1):
                yield (i, j)

    for u, v in edge_pairs():
        if cnt == K:
            break
        edges.append((u, v))
        cnt -= 1

    print(len(edges))
    stdout.writelines(f"{u} {v}\n" for u, v in edges)

if __name__ == "__main__":
    main()