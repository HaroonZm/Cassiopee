def num():
    return int(input())
def nums():
    return list(map(int,input().split()))
"""
A,B = nums()
P,Q,R = nums()

first_distance = P * B
pre_runned = (B - A) * Q
time = B + (first_distance - pre_runned) / (R + Q)
print(time)
"""
"""
N = num()
randoms = nums()
ans = 0
for i in range(N):
    today = randoms[i]
    if i == 0:
        continue
    if today > randoms[i-1]:
        ans += 1
print(ans)
"""
"""
N = num()
members = []
for i in range(N):
    members.append(input())

ans = members.count("E869120")
print(ans)
"""
"""
N = num()
V = nums()
V.sort(reverse=True)
ans = 0
for i in range(N):
    Vi = V[i]
    ans += (Vi - i -1)
print(ans)
"""

N = num()
A = nums()
ans_max = N
ans_min = 0
old_i = 0
for i in A:
    if not i > old_i:
        ans_min += 1
    old_i = i
ans_min += 1
print(ans_min)
print(ans_max)