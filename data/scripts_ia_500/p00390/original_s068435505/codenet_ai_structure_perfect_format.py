n = int(input())
aw = [[0, 0] for _ in range(n)]
a_values = list(map(int, input().split()))
w_values = list(map(int, input().split()))
for i, a in enumerate(a_values):
    aw[i][0] = a
for i, w in enumerate(w_values):
    aw[i][1] = w
migimin = 1001
hidarimin = 1001
for a, w in aw:
    if a:
        hidarimin = min(hidarimin, w)
    else:
        migimin = min(migimin, w)
if hidarimin > 1000 or migimin > 1000:
    print(0)
else:
    print(hidarimin + migimin)