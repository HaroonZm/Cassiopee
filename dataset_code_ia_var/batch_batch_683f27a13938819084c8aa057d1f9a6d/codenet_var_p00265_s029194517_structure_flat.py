N_Q = raw_input().split()
N = int(N_Q[0])
Q = int(N_Q[1])
c = [int(x) for x in raw_input().split()]
mxc = max(c)
p = [0] * (mxc + 1)
for i in c:
    p[i] = 1
l = [0] * (mxc + 1)
num = 0
i = 0
while i <= mxc:
    l[i] = num
    if p[i]:
        num = i
    i += 1
i = 0
while i < Q:
    q = int(raw_input())
    sp = mxc
    ans = 0
    while True:
        r = sp % q
        if r > ans:
            ans = r
        if sp - r <= 0:
            break
        sp = l[sp - r]
    print ans
    i += 1