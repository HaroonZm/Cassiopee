t = int(input())
dice = []
for _ in range(t):
    n, m = map(int, input().split())
    faces = []
    total_r = 0.0
    for __ in range(m):
        v, r = input().split()
        v = int(v)
        r = float(r)
        faces.append((v, r))
        total_r += r
    dice.append((n, m, faces, total_r))

p, q = map(int, input().split())
faces = []
total_r = 0.0
for _ in range(q):
    v, r = input().split()
    v = int(v)
    r = float(r)
    faces.append((v, r))
    total_r += r
leader = (p, q, faces, total_r)

def expected_value(faces, total_r):
    if total_r == 0:
        return 0.0
    s = 0.0
    for v, r in faces:
        s += v * r
    return s / total_r

leader_ev = expected_value(leader[2], leader[3])
flag = False
for d in dice:
    ev = expected_value(d[2], d[3])
    if ev - leader_ev > 0.0000001:
        flag = True
        break

if flag:
    print("YES")
else:
    print("NO")