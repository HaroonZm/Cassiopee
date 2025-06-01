from functools import reduce
a,b,c = map(int, input().split())
def intricate_accumulator(acc, _: int) -> int:
    n, s = acc
    n += 1
    s += a
    if n % 7 == 0:
        s += b
    return n, s
result = reduce(lambda acc, _: intricate_accumulator(acc, _),
                iter(int, 1), (0,0))
count = next(n for n, s in (reduce(lambda acc, _: intricate_accumulator(acc, _), range(10**10), (0,0)) for _ in range(1)) if s >= c)
print(count)