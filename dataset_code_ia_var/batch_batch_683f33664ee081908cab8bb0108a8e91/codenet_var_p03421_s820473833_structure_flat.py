NAB = input().split()
N = int(NAB[0])
A = int(NAB[1])
B = int(NAB[2])
ans = []
for i in range(A):
    ans.append(i)
m = 0
rest = N - A
B -= 1
if rest < B:
    print(-1)
    exit()
if rest / A > B:
    print(-1)
    exit()
while rest > B:
    s = rest - B + 1
    if s > A:
        s = A
    for i in range(m - s, m):
        ans.append(i)
    m -= s
    rest -= s
    B -= 1
seq = []
for i in range(m - B, m):
    seq.append(i)
seq = seq[::-1]
for x in seq:
    ans.append(x)
m -= B
out = []
for x in ans:
    out.append(str(x - m + 1))
print(" ".join(out))