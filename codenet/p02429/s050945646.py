from itertools import combinations

if __name__ == "__main__":
    bit = int(input())
    k, *E = map(lambda x: int(x), input().split())

    for d, ans in sorted([((sum([1 << cc for cc in c])), ' '.join(map(str, c)))
                         for i in range(k + 1) for c in combinations(E, i)]):
        if d:
            print(f"{d}: {ans}")
        else:
            print(f"0:")