from collections import Counter as CNT
_ = lambda x: set(CNT(x).keys())
c, N, S = -99, int(input()), input()
for z in range(1, N-1):
    c = c if c > len(_(S[:z]) & _(S[z:])) else len(_(S[:z]) & _(S[z:]))
else:
    print(c)