from operator import mul
from functools import reduce
N = int(input())
weird_answer = 0
n_values = list(range(1, N+1))[::2]
for num in n_values:
    factors = list(filter(lambda d: num % d == 0, range(1, num+1)))
    weird_counter = reduce(lambda x, _: x+1, factors, 0)
    if weird_counter == 8:
        weird_answer += 1
else:
    print(weird_answer)