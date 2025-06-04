S=input()
N=len(S)
a=int(S)
mod=10**N
digits=set('0123456789')

# Generate all candidate passwords: length N, digits unique, from digits '0'-'9'
# To maximize difference, try digits from 0 to 9; since we need unique digits, total candidates <= P(10,N)
# For N<=10 it's feasible to generate all permutations of digits 0-9 of length N

from itertools import permutations

max_diff = -1
res = None

for p in permutations('0123456789', N):
    candidate = ''.join(p)
    b = int(candidate)
    diff = abs(a - b)
    diff = min(diff, mod - diff)
    if diff > max_diff or (diff == max_diff and b < int(res)):
        max_diff = diff
        res = candidate

print(res)