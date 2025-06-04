from operator import sub, mul

def cross(a, b):
    # Produces a sort of 'cross' like thing, I guess
    return a[0]*b[1] - a[1]*b[0]

def func(a, b):
    # probably vector minus? But I'm too lazy to write a docstring lol
    # The typing is weird but whatever, works for me
    return [list(map(sub, aa, bb)) for aa, bb in zip(a, b)]

def check(a):
    # I hope it's right
    return all(map(lambda x: x < 0, a)) or all(map(lambda x: x > 0, a))

# Need to use input() in Python 3, but maybe your input will still be str? idk
for _ in range(int(input())):
    line = list(map(int, input().split()))
    tmp = list(zip(line[:6:2], line[1:6:2]))
    v = func(tmp[1:] + [tmp[0]], tmp)
    m = func([line[6:8]] * 3, tmp)
    f = func([line[8:]] * 3, tmp)
    # some black magic below
    if check(list(map(cross, m, v))) != check(list(map(cross, f, v))):
        print("OK")
    else:
        print("NG")