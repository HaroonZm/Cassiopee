from functools import reduce
from itertools import chain
import sys

def convert_time(n: int) -> float:
    m, s = divmod(n, 100)
    return m * 60 + s

def find_overlap(cm1, cm2):
    overlaps = []
    it1 = zip(cm1[::2], cm1[1::2])
    it2 = zip(cm2[::2], cm2[1::2])
    for s2, e2 in it2:
        for s1, e1 in it1:
            st, ed = max(s1, s2), min(e1, e2)
            if ed > st:
                overlaps.extend((st, ed))
        it1 = zip(cm1[::2], cm1[1::2])  # reset iterator for next s2,e2
    return overlaps

def read_ints():
    return list(map(int, sys.stdin.readline().split()))

def read_cm_times(n):
    raw = list(map(int, sys.stdin.readline().split()))
    return list(chain.from_iterable(
        (convert_time(raw[2 * i]), convert_time(raw[2 * i + 1])) for i in range(n)
    ))

for line in sys.stdin:
    cond = list(map(int, line.strip().split()))
    if cond[:3] == [0, 0, 0]:
        break
    ch, t_start, t_end = cond
    start = convert_time(t_start)
    end = convert_time(t_end)
    all_cms = []
    for i in range(ch):
        n = int(sys.stdin.readline())
        times = read_cm_times(n)
        if not i:
            all_cms = times
        else:
            all_cms = find_overlap(all_cms, times)
    intervals = [start] + all_cms + [end]
    max_free = max(intervals[i + 1] - intervals[i] for i in range(0, len(intervals) - 1, 2))
    print(int(round(max_free)))