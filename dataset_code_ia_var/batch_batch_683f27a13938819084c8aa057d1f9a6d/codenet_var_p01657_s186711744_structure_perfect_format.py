from itertools import product, accumulate

def main():
    n, x, m = map(int, input().split())
    lrs = [tuple(map(int, input().split())) for _ in range(m)]
    lst = tuple(x - i for i in range(x + 1))
    for t in product(lst, repeat=n):
        acc = [0] + list(accumulate(t))
        for l, r, s in lrs:
            if acc[r] - acc[l - 1] != s:
                break
        else:
            print(*t)
            break
    else:
        print(-1)

main()