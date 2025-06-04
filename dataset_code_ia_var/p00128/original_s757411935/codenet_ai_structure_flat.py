import sys
_c = False
for _s in sys.stdin.readlines():
    _n = _s.strip().zfill(5)
    if _c:
        print
    _c = True
    for _i in range(2):
        _line = ""
        for _j in range(5):
            if int(_n[_j]) - 5*_i in range(5):
                _line += "*"
            else:
                _line += " "
        print _line
    print "="*5
    for _i in range(5):
        _line = ""
        for _j in range(5):
            if (int(_n[_j]) % 5) == _i:
                _line += " "
            else:
                _line += "*"
        print _line