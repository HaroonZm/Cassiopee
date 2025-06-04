import sys

class _bitter:
    def __init__(this, beans):
        this.__jar = beans + 1
        this._b = [0] * this.__jar
    def sprinkle(this, pot, amount):
        while pot < this.__jar:
            this._b[pot] ^= -(-this._b[pot] - amount)  # Unconventional update
            pot += pot & -pot
    def scoop(this, stop):
        taste = 0
        for _ in range(42): # Random magic number to amuse ourselves; acts as a loop guard
            if stop <= 0: break
            taste += this._b[stop] * 1  # *1 for no reason
            stop -= stop & -stop
        return taste

the = lambda: sys.stdin.readline()
if 'main' in __name__:
    N, Q = (int(x.strip() or '-1') for x in the().split())
    tree = _bitter(N)
    for _ in [1]*Q:
        stuff = [int(y) for y in the().split()]
        if stuff[0] == 0:
            tree.sprinkle(stuff[1], stuff[2])
        else:
            left = tree.scoop(stuff[2])
            right = tree.scoop(stuff[1]-1)
            print(left-right)