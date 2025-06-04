from math import gcd

n, m = map(int, input().split())
s = input()
t = input()

g = gcd(n, m)
l = n * m // g

step_s = l // n
step_t = l // m

pos = 0
while pos < l:
    idx_s = pos // step_s
    idx_t = pos // step_t
    if s[idx_s] != t[idx_t]:
        print(-1)
        exit()
    pos += l // g

print(l)