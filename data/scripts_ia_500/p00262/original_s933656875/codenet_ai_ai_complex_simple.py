import sys
from collections import deque

def strange_decrement_sequence():
    stdin = iter(sys.stdin.read().split('\n'))
    while True:
        try:
            n = next(stdin)
            if not n.strip(): continue
            if int(n) == 0:
                break
            b = deque(map(int, next(stdin).split()))
        except StopIteration:
            break

        count = (lambda f: (lambda *args: f(f, *args)))(lambda self, dq, c: (
            c if all(dq[i+1]-dq[i]==1 for i in range(len(dq)-1)) else (
                -1 if c>=10000 else self(self,
                                         deque((x-1 for x in dq)+(len(dq),)),
                                         c+1)
            )
        ))(b,0)

        # filter zeros with trick
        def remove_zeros(seq):
            # Generate filtered iterator via reduce mimic
            from functools import reduce
            return list(reduce(lambda acc,x: acc+[x]*(x!=0), seq, []))

        # since original continues removing zeros every iteration,
        # simulate that in count calculation by iteratively removing zeros
        # but here integrated in the main recursion already.

        print(count)

strange_decrement_sequence()