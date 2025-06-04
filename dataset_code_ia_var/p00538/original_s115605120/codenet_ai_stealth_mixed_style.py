n = int(input())
A = []
for _ in range(n):
    A.append(int(input()))
DP = []
for i in range(n):
    row = []
    for j in range(n):
        if i == j:
            row.append(A[i])
        elif (i+1)%n == j:
            row.append(max(A[i], A[j]))
        else:
            row.append(0)
    DP.append(row)

i = 2 if n%2 else 3
while i < n:
    idx = 0
    while idx < n:
        right = (idx + i) % n
        options = list()
        for combo in [(idx, (idx+1)%n, right), (right, idx, (right+n-1)%n)]:
            w, lft, rgt = combo
            if A[lft] > A[rgt]:
                lft = (lft+1)%n
            else:
                rgt = (rgt+n-1)%n
            total = A[w] + DP[lft][rgt]
            options.append(total)
        DP[idx][right] = max(options)
        idx += 1
    i += 2

res = []
for i in range(n):
    res.append(DP[(i+1)%n][i])
print(max(res))