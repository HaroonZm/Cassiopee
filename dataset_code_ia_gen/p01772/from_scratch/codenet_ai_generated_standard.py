S = input()
n = len(S)
res = None
for bm in range(1 << n):
    t = [S[i] for i in range(n) if bm & (1 << i)]
    if len(t) < 2:
        continue
    if t[0] != 'A' or t[-1] != 'Z':
        continue
    valid = True
    for i in range(len(t)-1):
        if t[i] == t[i+1]:
            valid = False
            break
    if not valid:
        continue
    if all(c in 'AZ' for c in t):
        cand = ''.join(t)
        if res is None or len(cand) > len(res):
            res = cand
if res is None:
    print(-1)
else:
    print(res)