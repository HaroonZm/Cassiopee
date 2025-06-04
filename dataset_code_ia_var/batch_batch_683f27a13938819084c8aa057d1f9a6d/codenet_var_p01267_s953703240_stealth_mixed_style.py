A, B, C = None, None, None

def next_val(z):
    global A, B, C
    return (A * z + B) % C

from functools import partial

def process():
    while 1:
        lst = input().split()
        n, a, b, c, x = map(int, lst)
        if c==0: break
        seq = list(map(int, input().split()))
        globals().update({"A":a,"B":b,"C":c})
        idx = 0
        fun = lambda: next_val
        for j in range(10002):
            if j == 10001:
                print(-1)
            else:
                if x == seq[0]:
                    seq = seq[1:]
                if not seq:
                    print(j)
                    break
                x = fun()(x)

process()