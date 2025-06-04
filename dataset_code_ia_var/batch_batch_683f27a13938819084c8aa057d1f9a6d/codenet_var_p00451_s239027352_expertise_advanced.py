from sys import stdin
from itertools import islice

def longest_common_substring_length(s: str, t: str) -> int:
    # Guarantee s is the longer string
    if len(s) < len(t):
        s, t = t, s
    ans = 0
    tlen = len(t)
    slen = len(s)
    for sp in range(tlen):
        # No longer possible to find a longer substring
        if tlen - sp <= ans:
            break
        for l in range(ans + 1, tlen - sp + 1):
            substr = t[sp:sp + l]
            if substr in s:
                ans = l
            else:
                # Since no longer substrings from this position can match, break
                break
    return ans

def input_pairs(stream):
    while True:
        lines = list(islice(stream, 2))
        if len(lines) < 2:
            return
        yield tuple(line.rstrip('\r\n') for line in lines)

for s, t in input_pairs(stdin):
    print(longest_common_substring_length(s, t))