from collections import defaultdict
from sys import stdin
from itertools import islice

MAX = 3652425
BUF = 10010
SIZE = MAX + BUF

def main():
    n, q = map(int, stdin.readline().split())
    lst = [tuple(map(int, stdin.readline().split())) for _ in range(n)]
    queries = [int(stdin.readline()) for _ in range(q)]

    restor = [0] * SIZE
    t0s = [0] * SIZE
    t1s = [0] * SIZE
    t2s = [0] * SIZE
    t3s = [0] * SIZE

    t1_cnt_save = defaultdict(int)
    t3_cnt_save = defaultdict(int)

    t1_cnt = 0
    t3_cnt = 0
    idx = 0

    def advance(target):
        nonlocal idx, t1_cnt, t3_cnt
        while idx < target:
            nxt = idx + 1
            t0s[nxt] += t0s[idx]
            t1_cnt -= t1_cnt_save[nxt]
            t1s[nxt] += t1s[idx] + t1_cnt
            t3_cnt -= t3_cnt_save[nxt]
            t3s[nxt] += t3s[idx] + 2 * t3_cnt
            t2s[nxt] += t2s[idx] + t3s[nxt]
            restor[nxt] = restor[idx] + 1 + t0s[idx] + t1s[idx] + t2s[idx]
            idx = nxt

    for w, t, x in lst:
        advance(MAX if w > restor[idx] else idx)
        if w <= restor[idx]:
            print(idx)
            if t == 0:
                t0s[idx] += 1
                t0s[idx + x] -= 1
            elif t == 1:
                t1_cnt += 1
                t1_cnt_save[idx + x] += 1
                t1s[idx] += 1
                t1s[idx + x] -= x
            elif t == 2:
                t3_cnt += 1
                t3_cnt_save[idx + x] += 1
                t3s[idx] += 1
                t3s[idx + x] -= (x << 1) - 1
                t2s[idx] += 1
                t2s[idx + x] -= x * x
        else:
            print("Many years later")

    for y in queries:
        advance(y)
        print(restor[y])

if __name__ == "__main__":
    main()