from functools import reduce
from itertools import product, count, islice
from collections import defaultdict

alpha = list(map(chr, range(ord('a'), ord('z')+1)))
gen_triple = lambda c1: ["".join(seq) + "a" for seq in product([c1], alpha, alpha)]
dic = defaultdict(list)
_ = list(map(lambda c: dic[c].extend(gen_triple(c)), alpha))

print("?" + reduce(lambda _, x: x, islice(dic["a"], len(dic["a"])), None))
dic["a"] = dic["a"][:-1]

used = set()
while True:
    s = input()
    cond = (s in used) or (s[0] != "a")
    print("!OUT" if cond else "?" + dic[s[-1]].pop())
    if cond: break
    used |= {s}