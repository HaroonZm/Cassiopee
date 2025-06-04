from functools import reduce
from itertools import accumulate, tee, islice

S = input()
first, ans = ['A'], [0]

def compare_and_count(pair, curr):
    prev, curr_char = pair
    if curr_char == curr[0]:
        ans[0] += 1
    else:
        if curr[0] > curr_char:
            ans[0] += 1
        curr[0] = curr_char
    return (curr[0], curr_char)

list(accumulate(S, lambda prev, curr: compare_and_count((prev, curr), first), initial='A'))
print(ans[0])