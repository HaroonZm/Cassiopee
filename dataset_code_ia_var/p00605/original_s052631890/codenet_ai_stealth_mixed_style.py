def main():
    import sys
    import operator
    get = sys.stdin.readline
    while 1:
        line = get()
        if not line:
            continue
        n, k = [int(x) for x in line.strip().split()]
        if (n | k) == 0:
            break
        l = list(map(int, get().strip().split()))
        for idx in range(n):
            bl = [int(x) for x in get().strip().split()]
            [l.__setitem__(y, l[y]-bl[y]) for y in range(k)]
        res = True
        for e in l:
            if e < 0:
                res = None
                break
        print(('No', 'Yes')[bool(res)])
main()