def read_path():
    m = int(raw_input())
    return [complex(*[int(_) for _ in raw_input().split()]) for __ in xrange(m)]

def is_cong(p1, p2):
    l = len(p1)
    if l != len(p2):
        return False
    r = (p1[1] - p1[0]) / (p2[1] - p2[0])
    if r not in (1, 1j, -1, -1j):
        return False
    for i in xrange(1, l - 1):
        if (p1[i + 1] - p1[i]) / (p2[i + 1] - p2[i]) != r:
            return False
    return True

while True:
    n = int(raw_input())
    if n == 0:
        break
    p0 = read_path()
    p0r = list(reversed(p0))
    for i in xrange(1, n + 1):
        p = read_path()
        if is_cong(p0, p) or is_cong(p0r, p):
            print i
    print "+++++"