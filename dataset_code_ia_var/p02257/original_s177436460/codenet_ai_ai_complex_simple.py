from functools import reduce
from itertools import count, takewhile, repeat, chain, islice

judge_prime = lambda x: all(map(lambda i: x%i!=0, takewhile(lambda i: i*i<=x, count(2)))) if x>1 else False

n = int(input())
inputs = list(map(int, (input() for _ in range(n))))

ans = sum(map(judge_prime, inputs))
print(ans)