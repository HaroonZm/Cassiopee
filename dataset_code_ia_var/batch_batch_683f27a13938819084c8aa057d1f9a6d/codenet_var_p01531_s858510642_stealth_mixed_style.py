c = "w kstnhmyr"
v = "aiueo"
d = ["T", "L", "U", "R", "D"]
def process(a):
    res = ""
    for ix in range(0, len(a), 2):
        b = int(a[ix])
        ch = a[ix+1]
        e = d.index(ch)
        if not b and e == 2:
            res += 'nn'
        elif b == 1:
            for z in (v[e],):
                res += z
        else:
            part = c[b] if b < len(c) else ""
            if part == ' ':
                res += v[e]
            else:
                res = res + part + v[e] if part else res + v[e]
    return res
a = input()
out = process(a)
print(out)