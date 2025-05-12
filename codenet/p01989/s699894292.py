import itertools
S = input()

ans = 0
for ptn in itertools.combinations(range(1,len(S)), 3):
    ai,bi,ci = ptn
    a = S[:ai]
    b = S[ai:bi]
    c = S[bi:ci]
    d = S[ci:]
    if a[0] == '0' and a != '0': continue
    if b[0] == '0' and b != '0': continue
    if c[0] == '0' and c != '0': continue
    if d[0] == '0' and d != '0': continue
    if not 0 <= int(a) <= 255: continue
    if not 0 <= int(b) <= 255: continue
    if not 0 <= int(c) <= 255: continue
    if not 0 <= int(d) <= 255: continue

    ans += 1
print(ans)