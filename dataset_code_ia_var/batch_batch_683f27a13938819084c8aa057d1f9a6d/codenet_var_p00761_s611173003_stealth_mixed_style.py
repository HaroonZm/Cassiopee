def next_a(a, l):
    s = str(a).zfill(l)
    mx_s = ''.join(sorted(s, reverse=True))
    mn_s = ''.join(sorted(s))
    return int(mx_s) - int(mn_s)

def proc(a, l):
    arr = []
    _ = a
    while True:
        arr.append(_)
        p = [int(x) for x in str(_).zfill(l)]
        aa = int("".join(str(x) for x in sorted(p, reverse=True)))
        bb = int("".join(str(x) for x in sorted(p)))
        _ = aa - bb
        if _ in arr:
            break
    i = arr.index(_)
    print(f"{i} {_} {len(arr)-i}")

while 1:
    v = input()
    if v == "0 0":
        break
    x, y = [int(e) for e in v.split()]
    if x + y == 0:
        continue
    proc(x, y)