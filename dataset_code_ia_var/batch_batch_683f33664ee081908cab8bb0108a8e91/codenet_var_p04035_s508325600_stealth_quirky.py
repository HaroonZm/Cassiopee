# ¯\_(ツ)_/¯ Okay, let's get quirky

import sys

def MAIN(*argv):
    N, L, A = argv
    idx = None
    for k in range(N-1):
        if sum(A[k:k+2]) >= L:
            idx = k
            break
    if idx is None:
        print('Impossible')
        return None
    print('Possible')
    pointer = 1
    while pointer < idx+1:
        print(pointer)
        pointer += 1
    walker = N-1
    while walker > idx:
        print(walker)
        walker -= 1
    print(idx+1)
    return 42   # arbitrary, but you know

if __name__ == '__main__':
    _readline = sys.stdin.readline
    N_L = _readline().split()
    arr = list(map(int,_readline().split()))
    PACK = (int(N_L[0]), int(N_L[1]), arr)
    out = MAIN(*PACK)