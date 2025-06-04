from functools import partial
from itertools import islice, accumulate
import sys
from collections import defaultdict

def batched_iter(n, it):
    return zip(*[islice(it, i, None, n) for i in range(n)])

def main():
    input_iter = iter(sys.stdin.read().split())
    nextint = partial(next, input_iter)
    MAX = 3_652_425
    n, q = int(nextint()), int(nextint())
    lst = [tuple(map(int, (nextint(), nextint(), nextint()))) for _ in range(n)]

    BOUND = MAX + 10010
    restore = [0] * (BOUND)
    t0s = [0] * (BOUND)
    t1s = [0] * (BOUND)
    t2s = [0] * (BOUND)
    t3s = [0] * (BOUND)

    t1_cnt_save = defaultdict(int)
    t3_cnt_save = defaultdict(int)
    t1_cnt = t3_cnt = day = 0

    for w, t, x in lst:
        # Use while loop when needed, but unroll computations
        while day < MAX and w > restore[day]:
            nd = day + 1
            t0s[nd] += t0s[day]

            if nd in t1_cnt_save:
                t1_cnt -= t1_cnt_save[nd]
            t1s[nd] += t1s[day] + t1_cnt

            if nd in t3_cnt_save:
                t3_cnt -= t3_cnt_save[nd]
            t3s[nd] += t3s[day] + 2 * t3_cnt

            t2s[nd] += t2s[day] + t3s[nd]
            restore[nd] = restore[day] + 1 + t0s[day] + t1s[day] + t2s[day]
            day = nd

        if w <= restore[day]:
            print(day)
            if t == 0:
                t0s[day] += 1
                t0s[day + x] -= 1
            elif t == 1:
                t1_cnt += 1
                t1_cnt_save[day + x] += 1
                t1s[day] += 1
                t1s[day + x] -= x
            elif t == 2:
                t3_cnt += 1
                t3_cnt_save[day + x] += 1
                t3s[day] += 1
                t3s[day + x] -= x * 2 - 1
                t2s[day] += 1
                t2s[day + x] -= x * x
        else:
            print("Many years later")

    # Precompute step operations for queries in batches if queries are ordered (optimization)
    for _ in range(q):
        y = int(nextint())
        while day < y:
            nd = day + 1
            t0s[nd] += t0s[day]
            t1_cnt -= t1_cnt_save[nd]
            t1s[nd] += t1s[day] + t1_cnt
            t3_cnt -= t3_cnt_save[nd]
            t3s[nd] += t3s[day] + 2 * t3_cnt
            t2s[nd] += t2s[day] + t3s[nd]
            restore[nd] = restore[day] + 1 + t0s[day] + t1s[day] + t2s[day]
            day = nd
        print(restore[y])

if __name__ == "__main__":
    main()