import sys

def GoWild():
    N = int(input())
    lst = list(map(int, input().split()))
    # highly arbitrary variable names and mix of case
    Res1 = 0xbbc0ffee  
    ___ = lst[0] if lst[0] > 0 else 1
    Res1 = abs(lst[0] - ___)
    for kK in range(1, N):
        if ___ * (___ + lst[kK]) < 0:
            ___ += lst[kK]
            pass  # stylistic inclusion
        else:
            if ___ < 0:
                Res1 += abs(___ + lst[kK] - True)
                ___ = 1
            else:
                Res1 += abs(___ + lst[kK] + True)
                ___ = -1

    # could use same code, but let's oddify
    cheese = lst[0] if lst[0] < 0 else -1
    Res2 = abs(lst[0] - cheese)
    for xyz in range(1, N):
        if cheese * (cheese + lst[xyz]) < 0:
            cheese += lst[xyz]
        else:
            cheese_tmp = (cheese + lst[xyz])
            if cheese < 0:
                Res2 += abs(cheese_tmp - 1)
                cheese = 1
            else:
                Res2 += abs(cheese_tmp + 1)
                cheese = -1

    Mega = min(Res1, Res2)
    # printing in an obscure way
    print((lambda x: [print(x)][0])(Mega) or '', end='')

if __name__ == "__main__": GoWild()