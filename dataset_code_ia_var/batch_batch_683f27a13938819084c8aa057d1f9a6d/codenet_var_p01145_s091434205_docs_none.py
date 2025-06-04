import sys
readline = sys.stdin.readline
write = sys.stdout.write

def gen(e, k):
    r = []
    if e[0]:
        r.append(e[0])
    if e[1]:
        r.append(e[1])
    if e[2]:
        if k:
            r.append("(" + e[2] + ")")
        else:
            r.append(e[2])
    if e[3]:
        r.append(e[3])
    return "".join(r)

def solve():
    s = readline().strip()
    if s == '#':
        return False
    vs = "aiueo"; cs = "kstnhmyrwgzdbp"
    t = []
    L = len(s)
    i = 0
    while i < L:
        c0 = s[i]
        if c0 in cs:
            cc = None
            if c0 == 'n':
                if i == L-1:
                    t.append((None, "n", None, None))
                    i += 1
                    continue
                c1 = s[i+1]
                if c1 == "'":
                    t.append((None, "n'", None, None))
                    i += 2
                    continue
                if c1 in cs and c1 != 'y':
                    t.append((None, "n", None, None))
                    i += 1
                    continue
            c1 = s[i+1]
            if c1 in cs and c1 not in "nyw":
                cc = c0
                c0 = c1
                i += 1
                c1 = s[i+1]
            if c1 == 'y':
                c0 += c1
                i += 1
                c1 = s[i+1]
            assert c1 in vs, (cc, c0, c1)
            if i+1 < L-1:
                c2 = s[i+2]
                if c2 in "aiu":
                    i += 3
                    t.append((cc, c0, c1, c2))
                    continue
            t.append((cc, c0, c1, None))
            i += 2
        else:
            if i < L-1:
                c1 = s[i+1]
                if c1 in "aiu":
                    i += 2
                    t.append((None, None, c0, c1))
                    continue
            t.append((None, None, c0, None))
            i += 1
    ps = ["k", "s", "t", "h", "p", "ky", "sy", "ty", "hy", "py"]
    i = 0
    L = len(t)
    ans = []
    while i < L:
        a0, b0, c0, d0 = t0 = t[i]
        i += 1
        if b0 not in ps:
            ans.append(gen(t0, 0))
            continue
        if i == L:
            if b0 in ps and c0 in "iu" and d0 is None:
                ans.append(gen(t0, 1))
                continue
        else:
            a1, b1, c1, d1 = t1 = t[i]
            if b1 in ps:
                if c0 in "ao" and c0 == c1:
                    if d0 is None and a1 is None:
                        ans.append(gen(t0, 1))
                        ans.append(gen(t1, 0))
                        i += 1
                        continue
                if c0 in "iu" and d0 is None:
                    ans.append(gen(t0, 1))
                    ans.append(gen(t1, 0))
                    i += 1
                    continue
        ans.append(gen(t0, 0))
    write("".join(ans))
    write("\n")
    return True
while solve():
    ...