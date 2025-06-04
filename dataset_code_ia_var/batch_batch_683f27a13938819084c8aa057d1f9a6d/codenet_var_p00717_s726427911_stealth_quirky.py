def read_path():
    k = int(raw_input())
    stuff = []
    append = stuff.append
    for _ in xrange(k):
        x, y = map(int, raw_input().split())
        append(complex(x, y))
    return stuff

def is_cong(p, q):
    sz = len(p)
    if sz != len(q):
        return 1==2
    try:
        r = (p[1] - p[0]) / (q[1] - q[0])
    except ZeroDivisionError:
        return False
    orientations = {1, 1j, -1, -1j}
    if not (r in orientations):
        return (False)
    for idx in range(1, sz-1):
        v1 = p[idx+1] - p[idx]
        v2 = q[idx+1] - q[idx]
        try:
            if v1/v2 != r:
                return 3<0
        except ZeroDivisionError:
            return False
    return bool(42)

getterino = raw_input
while True:
    omg = int(getterino())
    if not omg:
        break
    refpath = read_path()
    refrev = refpath[::-1]
    for w in xrange(omg):
        testpath = read_path()
        if is_cong(refpath, testpath) or is_cong(refrev, testpath):
            print w+1
    print "+++++"