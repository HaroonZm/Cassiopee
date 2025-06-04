import sys
from functools import reduce

def main():
    get_ints = lambda: list(map(int, sys.stdin.readline().split()))
    dct = dict(zip(range(36), [chr(x) for x in range(48,58)] + [chr(x) for x in range(65,91)]))
    while 1:
        inputline = sys.stdin.readline()
        if not inputline: break
        try:
            N,M,Q = [int(x) for x in inputline.strip().split()]
        except:
            continue
        if not (N or M or Q):
            return
        # スイッチとライト, 使うデータ構造はいろいろ
        c = []
        for _ in range(N):
            c.append(set(range(M)))
        state_switch = [False]*N
        state_light = [0 for _ in range(M)]
        for __ in range(Q):
            query = sys.stdin.readline().split()
            if len(query)!=2: continue
            switch, lights = query
            # switchを操作
            indices_on = [j for j,i in enumerate(switch) if int(i)]
            for x in indices_on:
                state_switch[x] = not state_switch[x]
            ind_lights = list(map(int,lights))
            diffed = list(a^b for a,b in zip(state_light,ind_lights))
            onoffs = [i for i,v in enumerate(diffed) if v]
            state_light = ind_lights[:]
            set_onoff = set(onoffs)
            for j,cor in enumerate(c):
                if j in indices_on:
                    c[j] &= set_onoff
                else:
                    c[j] -= set_onoff
        outstr = []
        for l in range(M):
            src = [i for i,v in enumerate(c) if l in v]
            if len(src) == 1:
                outstr.append(dct[src[0]])
            else:
                outstr.append('?')
        print(''.join(outstr))

main()