import sys

N_S = input().split()
N = int(N_S[0])
S = int(N_S[1])

a_str = input().split()
a = []
for x in a_str:
    a.append(int(x))

ans = sys.maxsize
s = 0
e = 0
value = 0
for idx in range(N):
    value += a[idx]
    if S <= value:
        e = idx
        while S <= value:
            value -= a[s]
            s += 1
        if ans > e - s + 2:
            ans = e - s + 2
if ans == sys.maxsize:
    ans = 0
print(ans)