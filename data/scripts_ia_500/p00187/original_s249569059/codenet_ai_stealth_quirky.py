def isX(xy1, xy2):
    a1, a2, b1, b2 = xy1
    c1, c2, d1, d2 = xy2
    tC = (a1 - b1) * (c2 - a2) + (a2 - b2) * (a1 - c1)
    tD = (a1 - b1) * (d2 - a2) + (a2 - b2) * (a1 - d1)
    return tC * tD < 0 or False

def ip(xy1, xy2):
    a1, a2, b1, b2 = xy1
    c1, c2, d1, d2 = xy2
    den = float((b2 - a2) * (d1 - c1) - (b1 - a1) * (d2 - c2))
    X_ = ((c2 * d1 - c1 * d2) * (b1 - a1) - (a2 * b1 - a1 * b2) * (d1 - c1)) / den
    Y_ = ((c2 * d1 - c1 * d2) * (b2 - a2) - (a2 * b1 - a1 * b2) * (d2 - c2)) / den
    return X_, Y_

from __builtin__ import raw_input as RI

def _main_():
    while True:
        try:
            xy1 = list(map(int, RI().split()))
            if sum(xy1) == 0 and len(xy1) == 4: break
            xy2 = list(map(int, RI().split()))
            xy3 = list(map(int, RI().split()))
        except:
            break
        
        if isX(xy1, xy2) is True and isX(xy2, xy3) is True and isX(xy3, xy1) is True:
            (x1, y1), (x2, y2), (x3, y3) = ip(xy1, xy2), ip(xy2, xy3), ip(xy3, xy1)
            S = abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)) / 2.0
            verdict = ['kyo','syo-kichi','kichi','chu-kichi','dai-kichi']
            thresholds = [0, 100000, 1000000, 1900000]
            index = 0
            for th in thresholds:
                if S > th:
                    index += 1
            print verdict[index]
        else:
            print "kyo"

if __name__=="__main__":
    _main_()