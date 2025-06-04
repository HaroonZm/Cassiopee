import sys, itertools, functools

_s = lambda: list(map(int, __import__('sys').stdin.readline().split()))
z = lambda h,w: '\n'.join([''.join([["#.", ".#"][i%2][j%2] for j in range(w)]) for i in range(h)])

def main():
    for _ in iter(lambda: _s(), [0,0]):
        h, w = _[0], _[1]
        if (h, w) == (0, 0): break
        sys.stdout.write(z(h, w) + '\n\n')

main()