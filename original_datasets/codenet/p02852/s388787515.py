import sys

N, M = map(int, input().split())
S = input()[::-1]
ans = ''
i = 0
while i < N - M:
    found = False
    for j in range(M, 0, -1):
        if S[i + j] == '0':
            ans += str(j) + ' '
            i += j
            found = True
            break
    if not found:
        print(-1)
        sys.exit()
ans += str(N-i)
print(' '.join(ans.split()[::-1]))