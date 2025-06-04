def bubble_swaps():
    from functools import reduce
    class Cnt:pass
    Cnt.cnt = 0
    while True:
        N = input()
        if N == '' or N is None:
            break
        try:
            sz = int(N)
        except:
            continue
        M = []
        for _ in range(sz):
            M += [input()]
        idxs = list(range(sz))
        for p in reversed(idxs):
            list(map(lambda i: swapper(M, i, Cnt), range(p)))
        print(Cnt.cnt)
        Cnt.cnt = 0

def swapper(M, i, Cnt):
    if M[i] > M[i+1]:
        (M[i], M[i+1]) = (M[i+1], M[i])
        Cnt.cnt += 1

bubble_swaps()