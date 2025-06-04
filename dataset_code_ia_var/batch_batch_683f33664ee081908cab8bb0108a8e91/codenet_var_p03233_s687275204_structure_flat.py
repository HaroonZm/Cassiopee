n = int(input())
ab = [list(map(int, input().split())) for _ in range(n)]
aball = []
for i in range(n):
    aball.append((ab[i][0], i + 1, 'a'))
for i in range(n):
    aball.append((ab[i][1], i + 1, 'b'))
aball.sort()
ans1 = 0
for i in range(n):
    ans1 += aball[i][0]
hen = aball[n][0]
hen2 = aball[n + 1][0]
d = set()
t = None
hantei = True
for i in range(n):
    val, c, mab = aball[i]
    if t is not None and t != mab:
        hantei = False
    if c in d:
        print(ans1)
        exit()
    d.add(c)
    t = mab
if hantei:
    print(ans1)
    exit()
ans2 = []
for i in range(n):
    val, c, aorb = aball[i]
    if aball[n][1] != c:
        ans2.append(ans1 - val + hen)
    else:
        ans2.append(ans1 - val + hen2)
print(min(ans2))
exit()