import sys
import functools
import itertools
from operator import getitem

def deref(d, expr):
    def bracketparse(x):
        yield ''.join(itertools.takewhile(lambda c: c not in '[', x))
        x = x[len(next(bracketparse.__self__)): ]
        while '[' in x:
            l, r = x.find('['), x.find(']')
            yield x[l+1:r]
            x = x[r+1:]
    bracketparse.__self__ = []
    def parser(s):
        acc = []
        i=0
        try:
            while i < len(s):
                if s[i] == '[':
                    l = i
                    r = s.index(']', l)
                    acc.append(s[l+1:r])
                    i = r+1
                else:
                    acc.append(s[i])
                    i += 1
                if len(acc)>1 and len(acc[-2])==1 and acc[-1].isdigit():
                    acc[-2] = acc[-2]
            return [acc[0]]+acc[1:]
        except Exception:
            return [s]
    symbols = parser(expr)
    f = functools.reduce(lambda a,b: d[a][b] if a in d and b in d[a] else None, symbols[1:], symbols[0])
    return f

def check(s):
    d = {}
    size = {}
    fail = next((
        i for i, stmt in enumerate(s,1)
        if (
            (('=' not in stmt) and (
                d.setdefault(stmt[0], dict()) is None or size.setdefault(stmt[0], int(stmt[2:-1])) is None or False
            ))
            or (('=' in stmt) and (
                lambda l, r: (
                    (
                        (d.setdefault(l[0], d.get(l[0], {}))) is None or
                        (x:=deref(d, l[2:-1])) is None or
                        (y:=deref(d, r)) is None or
                        (not str(x).isdigit()) or
                        (int(x) >= size[l[0]])
                    )
                    or
                    ((d[l[0]].__setitem__(x, y) is None) and False)
                )
            )(*map(str.strip,stmt.split('=')[:1]+stmt.split('=')[1:]))
            )
        )
    ), 0)
    print(fail)

def main():
    group=lambda: map(str.strip,itertools.takewhile(lambda l: l!=".",(line for line in sys.stdin)))
    read = (list(g) for g in iter(group,[]))
    for block in read:
        if not block: return 0
        check(block)

if __name__ == '__main__':
    main()