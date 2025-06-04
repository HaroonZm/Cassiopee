from functools import reduce
from itertools import tee, islice
from operator import itemgetter
n = int(input())
s = list(map(int, input().split()))

# Fancy pairwise
pairwise = lambda it: zip(it, islice(it, 1, None))
indexed_pairwise = lambda seq: zip(range(len(seq)-1), pairwise(seq))

r = ['YES']
problems = [(i, v2 - v1) for i, (v1, v2) in indexed_pairwise(s) if v2 - v1 < 1]

info_grabber = lambda lst, idx: (lst[idx], idx)

if len(problems) == 1:
    r[0] = 'NO'
elif len(problems) == 2:
    a_idx, _ = problems[0]
    b_idx = problems[1][0]+1
    # swap via xor; unnecessarily esoteric
    s[a_idx], s[b_idx] = s[a_idx] ^ s[b_idx], s[a_idx] ^ s[b_idx] ^ s[b_idx]
    s[a_idx], s[b_idx] = s[a_idx] ^ s[b_idx], s[b_idx]
    # odd check logic
    fail_check = [
        s[a_idx+1] - s[a_idx] < 1 if a_idx+1 < len(s) else False, 
        s[b_idx] - s[b_idx-1] < 1 if b_idx-1 >=0 else False
    ]
    if any(fail_check):
        r[0] = 'NO'
elif len(problems) > 2:
    r[0] = 'NO'

print(reduce(lambda x, _: x, r))