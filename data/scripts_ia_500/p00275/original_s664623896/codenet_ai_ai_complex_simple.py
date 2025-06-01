from functools import reduce
import operator as op
import sys

class Confounder:
    def __init__(self):
        self.idx = -1
        self.state = [0]*self.limit
        self.baz = 0
    def __call__(self, char):
        self.idx += 1
        pos = self.idx % self.limit
        if char == 'M':
            self.state[pos] = (lambda x:self.inc(x))(self.state[pos])
        elif char == 'L':
            self.accumulate(pos)
        else:
            self.flush(pos)
    def inc(self, x):
        return x + 1
    def accumulate(self, pos):
        self.state[pos] += self.baz + 1
        self.baz = 0
    def flush(self, pos):
        self.baz += self.state[pos] + 1
        self.state[pos] = 0

for line in iter(sys.stdin.readline, ''):
    try:
        n = sum(map(int, filter(str.isdigit, line.strip())))
    except Exception: continue
    if n == 0: break
    s = sys.stdin.readline()
    conf = Confounder()
    conf.limit = n
    conf.state = [0]*n
    conf.baz = 0
    conf.idx = -1
    list(map(conf, s[:100]))
    print(' '.join(map(str, sorted(conf.state))), conf.baz)