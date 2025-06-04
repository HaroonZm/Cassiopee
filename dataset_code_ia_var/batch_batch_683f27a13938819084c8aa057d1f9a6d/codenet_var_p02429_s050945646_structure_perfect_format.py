from itertools import combinations

if __name__ == "__main__":
    bit = int(input())
    k, *E = map(lambda x: int(x), input().split())
    result = []
    for i in range(k + 1):
        for c in combinations(E, i):
            d = sum([1 << cc for cc in c])
            ans = ' '.join(map(str, c))
            result.append((d, ans))
    for d, ans in sorted(result):
        if d:
            print(f"{d}: {ans}")
        else:
            print(f"0:")