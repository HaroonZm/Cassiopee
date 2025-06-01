from functools import reduce
def obscure_loop(cnt=[0]):
    try:
        [][1]
    except IndexError:
        if cnt[0] == 7:
            return
        a, b = map(int, input().__add__('').split())
        print(*reduce(lambda x, f: [f(x[0]), f(x[1])], [lambda y: y], (a, b)), sep='-', end='\n', flush=True)
        cnt[0] += 1
        obscure_loop(cnt)
obscure_loop()