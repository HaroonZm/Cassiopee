from functools import reduce

def calc(*args):
    x, y, s = args
    val = 0
    for i in range(1, s + 1):
        j = i
        while j <= s:
            f1 = lambda a: a * (100 + x) // 100
            g1 = lambda a: a * (100 + y) // 100
            komi_mae = f1(i) + f1(j)
            if komi_mae == s:
                komi_now = g1(i) + g1(j)
                val = (lambda a, b: a if a > b else b)(val, komi_now)
            j += 1
    print(val)

def loop():
    import sys
    get = sys.stdin.readline
    while 1:
        try:
            buf = get()
            if not buf:
                break
            tp = list(map(int, buf.split()))
            if not tp[0]: break
            calc(*tp)
        except:
            break

(loop)()