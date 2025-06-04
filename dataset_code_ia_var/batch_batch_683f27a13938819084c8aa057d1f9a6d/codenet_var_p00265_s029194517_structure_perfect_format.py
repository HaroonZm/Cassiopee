N, Q = map(int, raw_input().split())
c = map(int, raw_input().split())

mxc = max(c)
p = [0] * (mxc + 1)
for i in c:
    p[i] = 1

l = [0] * (mxc + 1)
num = 0
for i in range(mxc + 1):
    l[i] = num
    if p[i]:
        num = i

for i in range(Q):
    q = int(raw_input())
    sp = mxc
    ans = 0
    while 1:
        r = sp % q
        ans = max(ans, r)
        if sp - r <= 0:
            break
        sp = l[sp - r]
    print ans