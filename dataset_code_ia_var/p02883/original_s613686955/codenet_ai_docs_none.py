import sys

sys.setrecursionlimit(10 ** 6)
input = sys.stdin.readline

def main():
    n, k = map(int, input().split())
    aa = list(map(int, input().split()))
    ff = list(map(int, input().split()))
    aa.sort(reverse=True)
    ff.sort()
    l = -1
    r = aa[0] * ff[-1]
    while l + 1 < r:
        m = (l + r) // 2
        s = 0
        for a, f in zip(aa, ff):
            b = m // f
            s += max(a - b, 0)
            if s > k:
                l = m
                break
        else:
            r = m
    print(r)

main()