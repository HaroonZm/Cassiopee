import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
S = [0] + [int(x) - ord('0') for x in readline().rstrip()]
P = [int(x) for x in read().split()]

P += P

dp = [P]

for i in range(N+1):
    P = dp[i]
    newP = []
    dx = 1<<i
    for a,b in zip(P, P[dx:]):
        if a > b:
            a,b = b,a
        if S[b-a]:
            newP.append(b)
        else:
            newP.append(a)
    dp.append(newP)

answers = (x for x in P[:-1])
print('\n'.join(map(str, answers)))