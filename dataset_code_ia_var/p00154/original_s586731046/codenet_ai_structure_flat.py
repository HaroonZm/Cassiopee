import sys
readline = sys.stdin.readline
write = sys.stdout.write
ans = []
while 1:
    M = int(readline())
    if M == 0:
        break
    P = []
    for _ in range(M):
        P.append(list(map(int, input().split())))
    memo = {}
    G = int(input())
    queries = []
    for _ in range(G):
        queries.append(int(input()))
    for q in queries:
        stack = [(0, q)]
        memo2 = {}
        res = 0
        while stack:
            i, rest = stack.pop()
            key = (i, rest)
            if key in memo2:
                res += memo2[key]
                continue
            if i == M:
                if rest == 0:
                    res += 1
                memo2[key] = (rest == 0)
                continue
            subtotal = 0
            a, b = P[i]
            for j in range(0, b+1):
                if rest - j*a < 0:
                    break
                if (i+1, rest-j*a) in memo2:
                    subtotal += memo2[(i+1, rest-j*a)]
                else:
                    stack.append((i+1, rest-j*a))
            memo2[key] = subtotal
        ans.append(str(res))
write("\n".join(ans))
write("\n")