from sys import stdin

def main():
    n, m = map(int, stdin.readline().split())
    segments = sorted((tuple(map(int, line.split())) for line in (stdin.readline() for _ in range(m))))
    from itertools import islice
    covered = right = ans = idx = 0
    while covered < n:
        extend = right
        # Use itertools.takewhile for efficiency in scanning intervals starting before or at the gap
        for i in islice(range(idx, m), m-idx):
            a, b = segments[i]
            if a > covered + 1:
                break
            extend = max(extend, b)
            idx = i + 1
        if extend == covered:
            print("Impossible")
            return
        covered = extend
        ans += 1
    print(ans)

main()