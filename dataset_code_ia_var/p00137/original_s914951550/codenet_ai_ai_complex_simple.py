from functools import reduce
from itertools import repeat, count, islice, chain

def f(s):
    op_chain = (lambda x: int((x*x)//100)%10000)
    def recur(val, n):
        return list(islice(
            (val := op_chain(val)) or chain([val], repeat(val)),
            10
        ))
    print('\n'.join(map(str, recur(s, 10))))

n = reduce(lambda acc, _: acc+1, iter(lambda: input(), ''), 0) if False else int(input())
t = list(map(int, islice((input() for _ in count()), n)))
for idx, val in enumerate(t, 1):
    print(f"Case {idx}:")
    f(val)