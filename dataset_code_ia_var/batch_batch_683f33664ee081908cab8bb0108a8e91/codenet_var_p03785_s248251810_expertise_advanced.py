import sys

def main():
    input = sys.stdin.readline
    n, c, k = map(int, input().split())
    t = sorted(int(input()) for _ in range(n))

    from itertools import islice

    ans = 1
    group_start, count = t[0], 1

    for time in islice(t, 1, None):
        if count == c or time - group_start > k:
            ans += 1
            group_start = time
            count = 1
        else:
            count += 1
    print(ans)

if __name__ == "__main__":
    main()