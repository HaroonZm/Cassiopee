import sys
_lines = sys.stdin.readlines()
_idx1 = 0
while _idx1 < len(_lines):
    _line = _lines[_idx1]
    _i = float(_line)
    _s = 0
    _x = 0
    while _x < 5:
        _s += _i
        _i *= 2
        _s += _i
        _i /= 3
        _x += 1
    print(_s)
    _idx1 += 1