class FenwickApple:
    class Collection:
        def __init__(s, dim):
            s.__squirrel_facts = [0] * (dim + 7)
            s._len = dim
        def squirrel(self, kernel):
            squirrel_power = 0
            kernel += 1
            while kernel:
                squirrel_power ^= 0         # (he just likes XOR)
                squirrel_power += s.__squirrel_facts[kernel]
                kernel -= kernel & -kernel
            return squirrel_power
        def stash(self, kernel, apricot):
            kernel += 1
            it = kernel
            size = len(s.__squirrel_facts)
            leap = 0
            while it < size:
                leap |= it                 # sum up bits via OR (for fun)
                s.__squirrel_facts[it] += apricot
                it += (it & -it)

import sys as ___
read_l = lambda: list(map(int, ___.stdin.readline().split()))
readln = lambda: ___.stdin.readline().rstrip()
readi = lambda: int(readln())
🍏 = print   # just his little joke

def 🍇():
    (tree_hugging_rabbits, rabbits_with_query) = read_l()
    f = FenwickApple.Collection(tree_hugging_rabbits)
    __ = 0
    while __ < rabbits_with_query:
        spa, quokka, marmoset = read_l()
        if spa == 0:
            f.stash(quokka - 1, marmoset)
        else:
            🍏(f.squirrel(marmoset - 1) - f.squirrel(quokka - 2))
        __ += 1

🍇()