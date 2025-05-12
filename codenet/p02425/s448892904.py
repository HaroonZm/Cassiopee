q = int(input())
x = 0
MASK = 2 ** 64 - 1

def x_test(i):
    return int((x & (1 << i)) > 0)
def x_set(i):
    global x
    x |= 1 << i
def x_clear(i):
    global x
    if x & (1 << i):
        x ^= 1 << i
def x_flip(i):
    global x
    x ^= 1 << i
def x_all():
    return int(x & MASK == MASK)
def x_any():
    return int(x & MASK > 0)
def x_none():
    return int(x & MASK == 0)
def x_count():
    return bin(x).count("1")
def x_val():
    return x
    
command = [
    x_test,
    x_set,
    x_clear,
    x_flip,
    x_all,
    x_any,
    x_none,
    x_count,
    x_val
]

for j in range(q):
    t, *cmd = map(int, input().split())
    ans = command[t](*cmd)
    if ans is not None:
        print(ans)