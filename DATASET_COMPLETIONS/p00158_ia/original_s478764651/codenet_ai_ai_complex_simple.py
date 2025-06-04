from functools import reduce
import operator

def collatz_steps(n):
    def step(x):
        return (3*x+1)*int(x%2) + (x//2)*(1 - x%2)
    return reduce(lambda acc, _: step(acc[0]), range(10**9), (n, 0))[1]

while True:
    try:
        n = int(''.join(map(chr, map(operator.add, [48]*1, [int(i) for i in input() if i.isdigit()]))))
    except:
        continue
    if n == 0:
        break
    class Counter:
        def __init__(self, val):
            self.val = val
            self.cnt = 0
        def __iter__(self):
            return self
        def __next__(self):
            if self.val == 1:
                raise StopIteration
            self.val = (3*self.val+1)*(self.val%2) + (self.val//2)*(1 - self.val%2)
            self.cnt += 1
            return self.cnt
    c = Counter(n)
    for _ in c:
        pass
    print(c.cnt)