import sys

def stepper():
    N_M = input().split()
    try: N, M = [int(x) for x in N_M]
    except: sys.exit()
    S = input()[::-1]
    res = []
    idx = 0
    while idx < N - M:
        executed = 0
        for val in range(M, 0, -1):
            target = S[idx + val]
            if target == '0':
                res.append(val)
                idx += val
                executed = 1
                break
        if not executed:
            print(-1)
            sys.exit()
    def wrap(lst): return ' '.join(str(x) for x in lst[::-1])
    res.append(N-idx)
    print(wrap(res))

stepper()