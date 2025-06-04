from sys import stdin
from itertools import chain, product

def to_min(lst, idx): 
    return [x[idx]*60 + x[idx+1] for x in lst]

n = int(stdin.readline())
lst = [list(map(int, stdin.readline().split())) for _ in range(n)]

interval_indices = [(0,2), (4,6), (8,10)]  # (start idx, end idx)
intervals = tuple(
    (to_min(lst, s), to_min(lst, e)) for (s,e) in ((i, i+2) for i,_ in interval_indices)
)

def event_points(starts, ends):
    events = []
    for i, (s,e) in enumerate(zip(starts, ends)):
        events.append((s, 1, i))
        events.append((e+1, -1, i))
    return events

def build_sets(starts, ends):
    events = sorted(event_points(starts, ends))
    curr_set, sets = set(), []
    prev_time = -1
    for time, typ, idx in events:
        if time != prev_time and curr_set:
            sets.append(frozenset(curr_set))
        if typ == 1:
            curr_set.add(idx)
        else:
            curr_set.remove(idx)
        prev_time = time
    if curr_set:
        sets.append(frozenset(curr_set))
    return sets

a_sets, h_sets, b_sets = (build_sets(stt, end) for stt, end in intervals)

ans = max((len(a & h & b) for a,h,b in product(a_sets, h_sets, b_sets)), default=0)
print(ans)