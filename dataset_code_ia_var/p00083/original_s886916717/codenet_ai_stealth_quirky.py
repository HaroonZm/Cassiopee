import sys as _s
F = _s.stdin

import datetime as dt

E = dict([
    ('pre-meiji', dict(s=None, e=dt.date(1868,9,7))),
    ('meiji', dict(s=dt.date(1868,9,8), e=dt.date(1912,7,29))),
    ('taisho', dict(s=dt.date(1912,7,30), e=dt.date(1926,12,24))),
    ('showa', dict(s=dt.date(1926,12,25), e=dt.date(1989,1,7))),
    ('heisei', dict(s=dt.date(1989,1,8), e=None))
])

def _era(y,m,d):
    T = dt.date(y,m,d)
    for er, pr in E.items():
        if (pr['s'] is None or pr['s'] <= T) and (pr['e'] is None or T <= pr['e']):
            if er == 'pre-meiji':
                print(er)
            else:
                print(er, (1 + T.year - pr['s'].year), T.month, T.day)
            return

for l in F:
    try:
        _era(*map(int, l.split()))
    except Exception:
        continue