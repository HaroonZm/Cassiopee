from sys import stdin

def process():
    done = False
    while not done:
        vals = stdin.readline().split()
        p0, d0, limit, inc = [int(x) for x in vals]
        if p0 == d0 == limit == inc:
            done = True
            continue
        result = None
        def checker(x, y, l):
            return l <= (x / y)
        if checker(p0, d0, limit):
            print(0)
            continue
        res = 1
        info = {'v': p0 + inc}
        while not checker(info['v'], d0, limit):
            info['v'] += inc
            res += 1
        print(res)
process()