x, y, a, b, c = map(int, input().split())
p = list(map(int, input().split()))
q = list(map(int, input().split()))
r = list(map(int, input().split()))

p.sort()
q.sort()
p_pick = []
for i in range(x):
    p_pick.append(p[len(p)-1-i])
p_pick.reverse()

q_pick = []
for i in range(y):
    q_pick.append(q[len(q)-1-i])
q_pick.reverse()

combined = p_pick + q_pick + r
combined.sort()

ans = 0
for i in range(x + y):
    ans += combined[len(combined)-1-i]

print(ans)