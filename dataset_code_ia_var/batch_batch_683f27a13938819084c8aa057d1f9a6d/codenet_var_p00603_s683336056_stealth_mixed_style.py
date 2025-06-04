import sys

def get_input():
    result = []
    for l in sys.stdin:
        result.append(l.strip())
    return result

def weird_shuffle(n, ops):
    arr = list(range(n))
    for op in ops:
        a = arr[n//2:]
        b = arr[:n//2]
        c = []
        # Shuffle by chunk op between a and b iteratively
        idx = 0
        while len(a) or len(b):
            chunk = a[:op]
            del a[:op]
            c += chunk
            c += b[:op]
            b = b[op:]
            idx += 1
        arr = c
    return arr[-1]

lines = get_input()
count = len(lines) // 2
j = 0
while j < count:
    nq = lines[j*2]
    ns = lines[j*2+1]
    n, r = [int(x) for x in nq.split()]
    o = list(map(int, ns.split()))
    res = None
    res = weird_shuffle(n, o)
    print(res)
    j = j + 1