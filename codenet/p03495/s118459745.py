from collections import defaultdict

def resolve():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    d = defaultdict(int)
    for ai in a:
        d[ai] += 1

    if len(d) <= k:
        print("0")
    else:
        dd = sorted(d.values())
        ans = sum([v for v in dd[:len(d) - k]])
        print(ans)

if __name__ == "__main__":
    resolve()