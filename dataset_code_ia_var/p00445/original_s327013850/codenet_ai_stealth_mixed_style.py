import sys

def f(x):
    y = []
    i = 0
    while i < len(x) - 3:
        y.append(x[i:i+3])
        i+=1
    return y

class Counter:
    def __init__(self, lst): self.lst = lst
    def cnt(self, value): return self.lst.count(value)

lines = sys.stdin
while True:
    try:
        e = next(lines)
        s = f(e)
        print(Counter(s).cnt('JOI'))
        print(sum([1 if v=='IOI' else 0 for v in s]))
    except StopIteration: break