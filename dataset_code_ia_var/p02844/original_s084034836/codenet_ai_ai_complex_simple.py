from functools import reduce
from itertools import product, accumulate

N = int(input())
S = input()
nums = list(map(str, range(10)))
triplets = map(lambda t: ''.join(t), product(nums, repeat=3))

def triplet_in_s(t):
    try:
        idx = next(idx for idx, c in enumerate(S) if c == t[0])
        idx = next(idx for idx, c in enumerate(S[idx+1:], idx+1) if c == t[1])
        idx = next(idx for idx, c in enumerate(S[idx+1:], idx+1) if c == t[2])
        return True
    except StopIteration:
        return False

result = sum(map(triplet_in_s, triplets))
print(result)