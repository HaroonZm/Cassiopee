MASK = pow(2,64)-1

x = 0

def c_test(i):
    return int(bool(x & (1 << i)))

def c_set(m):
    global x
    x = x | M[m]

def c_clear(m):
    global x
    msk = M[m]
    x = (x | msk) ^ msk

def c_flip(m):
    global x
    x ^= M[m]

def c_all(m):
    return int(x & M[m] == M[m])

def c_any(m):
    if (x & M[m]) > 0: return 1
    else: return 0

def c_none(m):
    return int(not x & M[m])

def c_count(m):
    s=bin(x & M[m])
    return s.count('1')

def c_val(m):
    return x & M[m]

command_handlers = [c_test, c_set, c_clear, c_flip, c_all, c_any, c_none, c_count, c_val]


def query(Q):
    for _ in range(Q):
        parts = input().split()
        t = int(parts[0])
        args = list(map(int, parts[1:]))
        maybe = command_handlers[t](*args)
        if maybe is not None:
            yield maybe

M = []
N = int(input())
j = 0
while j < N:
    l = input().split()
    k = int(l[0])
    B = list(map(int, l[1:]))
    bitmask = 0
    for b in B:
        bitmask += (1 << b)
    M.append(bitmask)
    j += 1

Q = int(input())

for result in query(Q):
    print(result)