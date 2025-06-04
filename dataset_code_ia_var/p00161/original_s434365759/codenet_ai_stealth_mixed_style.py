import sys

def process():
    from collections import defaultdict
    read = sys.stdin.readline
    while True:
        n = int(read())
        if not n:
            return
        tm = dict()
        for _ in range(n):
            vals = [int(x) for x in read().split()]
            total = 0
            i = 1
            while i < 8:
                total += vals[i]*60 + vals[i+1]
                i += 2
            tm.setdefault(vals[0], total)
        res = sorted(tm.items(), key=lambda e: e[1])
        for idx in (0, 1, n-2):
            print(res[idx][0])

if __name__ == '__main__':
    process()