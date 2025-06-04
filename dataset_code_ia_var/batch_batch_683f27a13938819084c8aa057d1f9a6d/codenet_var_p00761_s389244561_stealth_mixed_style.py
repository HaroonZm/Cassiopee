import sys

def kaprek_value(a, l):
    hist = dict()
    counter = 0
    hist[a] = counter
    while 1:
        counter += 1
        s = str(a).rjust(l, '0')
        digits = [d for d in s]
        digits.sort()
        big = "".join(reversed(digits))
        small = "".join(digits)
        res = int(big) - int(small)
        if res in hist.keys():
            print "%d %d %d" % (hist[res], res, counter - hist[res])
            return
        else:
            hist[res] = counter
        a = res

getNumbers = lambda: map(int, raw_input().split())
while True:
    pair = getNumbers()
    if (pair[0] | pair[1]) == 0: break
    a = pair[0]
    l = pair[1]
    kaprek_value(a, l)