import sys

def bitmask_from_list(lst):
    mask = 0
    for i, v in enumerate(lst):
        if v == 1:
            mask |= 1 << i
    return mask

for line in sys.stdin:
    if not line.strip():
        continue
    n,c = map(int,line.split())
    if n == 0 and c == 0:
        break
    a = [0]*n
    for i in range(n):
        a[i] = bitmask_from_list(list(map(int, sys.stdin.readline().split())))
    b = [0]*c
    for i in range(c):
        b[i] = bitmask_from_list(list(map(int, sys.stdin.readline().split())))
    # dp[i][state]: i-th beat, state=bitmask of lit buttons, max score
    from collections import defaultdict
    dp = [defaultdict(lambda:-1) for _ in range(n+1)]
    dp[0][0]=0
    for i in range(n):
        for lit,score in dp[i].items():
            lit_new = lit | a[i]
            for btn in b:
                pressed = lit_new & btn
                new_lit = lit_new & (~btn)
                add_score = bin(pressed).count('1')
                if dp[i+1][new_lit]<score+add_score:
                    dp[i+1][new_lit]=score+add_score
    print(max(dp[n].values()))