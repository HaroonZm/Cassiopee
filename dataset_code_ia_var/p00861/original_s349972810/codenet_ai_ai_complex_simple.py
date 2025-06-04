from functools import reduce
from operator import itemgetter, eq

class CustomArray:
    def __init__(self, sz):
        self.sz = sz
        self.vals = dict.fromkeys(range(sz), None)
    def size(self):
        return reduce(lambda acc, x: acc+1, self.vals, 0)
    def assign(self, idx, val):
        return (lambda c: (self.vals.__setitem__(idx, val), True)[1] if c else False)(
            all([
                idx is not None,
                val is not None,
                idx in self.vals
            ])
        )
    def get(self, idx):
        return (lambda x: x if x is not None else None)(self.vals.get(idx)) \
            if (idx is not None and idx in self.vals) else None

class Arrays:
    def __init__(self):
        self.arrays = {}
    def declare(self, arrName, sz):
        return (arrName not in self.arrays)*(sz is not None)*(self.arrays.setdefault(arrName, CustomArray(sz)) or True)
    def assign(self, arrName, idx, val):
        return self.arrays.get(arrName, lambda *_: False).assign(idx, val) if arrName in self.arrays else False
    def get(self, arrName, idx):
        return (self.arrays.get(arrName) or (lambda *_: None)).get(idx) if arrName in self.arrays else None

def resolve(expression):
    global arrays
    # Remove all whitespace for fancy parsing
    expr = ''.join(expression.split())
    def nestfind(e):
        level, start = 0, None
        for i, c in enumerate(e):
            if c == '[':
                if start is None: start = i
                level += 1
            elif c == ']':
                level -= 1
                if level == 0: return (start, i)
        return (None, None)
    # non-array integer
    if '[' not in expr:
        return int(expr)
    arrName = expr[0]
    idxStart, idxEnd = nestfind(expr)
    idx = resolve(expr[idxStart+1:idxEnd])
    return arrays.get(arrName, idx)

def processAssignment(command):
    global arrays
    eqIdx = command.index('=')
    l, r = command[:eqIdx], command[eqIdx+1:]
    arrName = l[0]
    idx = resolve(l[l.index('[')+1 : l.rindex(']')])
    return arrays.assign(arrName, idx, resolve(r))

def processDeclaration(arrStr):
    global arrays
    arrName = arrStr[0]
    size = int(arrStr[arrStr.index('[')+1 : arrStr.rindex(']')])
    return arrays.declare(arrName, size)

if __name__ == '__main__':
    import sys
    from itertools import count, takewhile
    while True:
        cmdseq = list(
            takewhile(lambda line: line!='.', map(str.strip, iter(input, '')))
        )
        if not cmdseq:
            break
        arrays = Arrays()
        errLine = next((i+1 for i,cmd in enumerate(cmdseq)
                        if (processAssignment(cmd) if '=' in cmd else processDeclaration(cmd))==False),
                       0)
        print(errLine)