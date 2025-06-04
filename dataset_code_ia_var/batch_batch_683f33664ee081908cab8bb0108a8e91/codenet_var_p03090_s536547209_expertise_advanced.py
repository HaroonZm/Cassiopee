from sys import stdin
from itertools import combinations, product

def main():
    N = int(stdin.readline())
    ans = set()

    rng = range(1, N + 1)
    if N % 2 == 0:
        for i in rng:
            k = N - i + 1
            skip = {i, k}
            idx = [j for j in rng if j not in skip]
            ans.update({tuple(sorted((i, j))) for j in idx})
            ans.update({tuple(sorted((k, j))) for j in idx})
    else:
        ans.update((min(i, N), max(i, N)) for i in range(1, N))
        for i in range(1, N):
            k = N - i
            skip = {i, k}
            idx = [j for j in rng if j not in skip]
            ans.update({tuple(sorted((i, j))) for j in idx})
            ans.update({tuple(sorted((k, j))) for j in idx})

    print(len(ans))
    for a, b in ans:
        print(a, b)

if __name__ == "__main__":
    main()