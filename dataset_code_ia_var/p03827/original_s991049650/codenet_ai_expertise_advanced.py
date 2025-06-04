from itertools import accumulate

N = int(input())
S = input()
mapping = {'I': 1, 'D': -1}
rui = list(accumulate((mapping[c] for c in S), initial=0))
print(max(rui))