# AOJ Volume4 0411
# http://judge.u-aizu.ac.jp/onlinejudge/description.jsp?id=0411

N, L = list(map(int, input().split()))
c = []
for _ in range(0, N):
    p, d = list(map(int, input().split()))
    c += [(p, d)]
c.sort()
masu = [p for p, d in c]
dir  = [d for p, d in c]

result = 0

score = 0
for j in range(0, N):
    if dir[j] == 0:
        score += masu[j] - j - 1
    elif dir[j] == 1:
        score -= masu[j] - j - 1
    masu[j] = j + 1
result = score

for i in range(N - 1, -1, -1):
    if dir[i] == 1:
        score += L - (N - i) - masu[i] + 1
    elif dir[i] == 0:
        score -= L - (N - i) - masu[i] + 1
    masu[i] = L - (N - i) + 1
    
    result = max(result, score)
print(result)