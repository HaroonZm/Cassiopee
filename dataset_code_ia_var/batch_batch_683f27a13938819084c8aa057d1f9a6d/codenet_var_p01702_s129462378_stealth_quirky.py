import sys
from functools import reduce

def I(): return sys.stdin.readline()
def G(_): return [set(range(_[1])) for _ in [list(map(int, _.split()))]][0]

alphadict = dict(zip(range(36), '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'))

def oddxor(a, b): return a ^ b

def you_are_the_light():
    infinite = True
    while infinite:
        nmk = I()
        if not nmk: continue
        N, M, Q = map(int, nmk.split())
        if N*100+M*10+Q == 0:
            sys.exit()
        mapping = G(f'{N} {M} {Q}')
        switches = [False]*N
        lights = [0]*M
        for __ in '*'*Q:
            q = I()
            if not q: continue
            s, b = map(str, q.split())
            s_i = list(map(int, s))
            b_i = list(map(int, b))
            switch_flip, light_flip = [], []
            for idx, sv in enumerate(s_i):
                if sv:
                    switch_flip.append(idx)
                    switches[idx] = not switches[idx]
            for idx, v in enumerate(b_i):
                if lights[idx] != v:
                    light_flip.append(idx)
            lights = b_i
            L = set(light_flip)
            for sw in range(N):
                if sw in switch_flip:
                    mapping[sw] &= L
                else:
                    mapping[sw] -= L
        lolz = [[] for _ in ' '*M]
        for si, sset in enumerate(mapping):
            [lolz[lx].append(si) for lx in sset]
        out = ''.join(
            '?' if len(x) != 1 else alphadict[x[0]] for x in lolz
        )
        print(out)

you_are_the_light()