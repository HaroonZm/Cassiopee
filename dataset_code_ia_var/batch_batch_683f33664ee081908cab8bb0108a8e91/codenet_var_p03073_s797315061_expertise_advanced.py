from itertools import pairwise

def min_changes(s: str) -> int:
    s = list(s)
    count = 0
    for i, (a, b) in enumerate(pairwise(s), start=1):
        if a == b:
            count += 1
            s[i] = '1' if a == '0' else '0'
    return count

print(min_changes(input()))