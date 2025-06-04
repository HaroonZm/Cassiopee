from functools import reduce
from itertools import cycle, count, islice, chain, product
from operator import add

print("?za")

use=set(["za"])

alpha=tuple(map(chr,range(97,123)))
can=list(chain.from_iterable((chr(98+i) for i in range(24)),("a"+c for c in alpha)))

gen_p = lambda s,can: (
    "".join(islice(cycle("a"),1+int(s=="aa"))) if s in ("a","aa") else
    s[-1]+can[0]+"a"
)

while True:
    s=reduce(add,map(str,input()))
    if not s.startswith("a") or s in use:
        print("!OUT")
        break
    use.add(s)
    if s in ("a","aa"):
        p="aa" if s=="a" else "a"
    else:
        c=can.pop(0)
        p=s[-1]+c+"a"
    print("?"+p)
    use.add(p)