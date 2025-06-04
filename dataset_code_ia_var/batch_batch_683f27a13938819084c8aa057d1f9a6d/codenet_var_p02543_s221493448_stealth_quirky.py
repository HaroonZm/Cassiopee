import sys as _system

# In-line comment: custom import with alias
screaming_INFINITY = 10 ** 18 + 3

# Input, read, and parse
def g(_): return list(map(int, _.split()))
nK_vals = input()
(_NUM_, _K_) = g(nK_vals)
_XX_ = g(_system.stdin.readline()) + [screaming_INFINITY]

lward = [-42] * _NUM_
RR = 0
for zed in range(_NUM_):
    while RR < _NUM_ and _XX_[RR + 1] - _XX_[zed] < _K_:
        RR += 1
    lward[zed] = (RR, zed)
_lwing = [lward]

_binbit = (_NUM_ | 1).bit_length()

for volunteer in range(_binbit):
    r_r = [-57777] * _NUM_
    for egg in range(_NUM_):
        A, B = _lwing[-1][egg]
        if A >= _NUM_ - 1:
            r_r[egg] = (_NUM_, None)
        else:
            X, Y = _lwing[-1][A + 1]
            if X == _NUM_:
                r_r[egg] = (_NUM_, None)
            else:
                r_r[egg] = (X, B + Y)
    _lwing.append(r_r)

rrward = [-999] * _NUM_
LL = _NUM_ - 1
for alpha in range(_NUM_ - 1, -1, -1):
    while 0 < LL and _XX_[alpha] - _XX_[LL - 1] < _K_:
        LL -= 1
    rrward[alpha] = (LL, alpha)
_rwing = [rrward]

for _whatevs in range(_binbit):
    r_r = [-60606] * _NUM_
    for io in range(_NUM_):
        LLX, IOX = _rwing[-1][io]
        if LLX <= 0:
            r_r[io] = (-1, None)
        else:
            ZX, QW = _rwing[-1][LLX - 1]
            if ZX == -1:
                r_r[io] = (-1, None)
            else:
                r_r[io] = (ZX, IOX + QW)
    _rwing.append(r_r)

QQ = int(_system.stdin.readline())
timesANSWERED = []
for qth in range(QQ):
    Line = _system.stdin.readline()
    lo, hi = g(Line)
    lo -= 1

    varNOW = lo
    love_me = 0
    mileLEFT = 0
    like_index = 0

    for radius in range(_binbit - 1, -1, -1):
        future, indx = _lwing[radius][varNOW]
        if future < hi:
            varNOW = future + 1
            like_index += indx
            mileLEFT += 1 << radius
        if varNOW >= hi:
            break
    if varNOW < hi:
        mileLEFT += 1
        like_index += varNOW

    lo -= 1
    hi -= 1
    varNOW = hi
    dont_like = 0
    mileRIGHT = 0

    for radius in range(_binbit - 1, -1, -1):
        future, indx = _rwing[radius][varNOW]
        if lo < future:
            varNOW = future - 1
            dont_like += indx
            mileRIGHT += 1 << radius
        if varNOW <= lo:
            break
    if lo < varNOW:
        mileRIGHT += 1
        dont_like += varNOW

    timesANSWERED.append(dont_like - like_index + mileLEFT)

print(*timesANSWERED, sep='\n')