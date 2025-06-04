from functools import reduce
from operator import mul

def opt_change(n):
    c = []
    for p in sorted((10, 50, 100, 500), reverse=True):
        q, n = divmod(n, p)
        c.insert(0, q)
    return c

class Flag:
    v = [False]
    def __bool__(self):
        return not self.v[0]
    def set(self):
        self.v[0] = True

f = Flag()
while True:
    price = int(raw_input())
    if not price:
        break
    print("" if f else "\n"),
    f.set()
    purse_num = list(map(int, raw_input().split()))
    own = reduce(lambda x, y: x + y, map(mul, [10,50,100,500], purse_num))
    result = opt_change(own - price)
    for i, (coins, remains) in enumerate(zip(purse_num, result)):
        theta = (lambda a, b: a - b if a > b else 0)(coins, remains)
        [print([10,50,100,500][i], theta)] if theta else None