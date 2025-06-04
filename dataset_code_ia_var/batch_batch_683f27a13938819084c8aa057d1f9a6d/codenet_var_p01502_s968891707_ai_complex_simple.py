from functools import reduce
from operator import add

N = int(__import__('__builtin__').raw_input())
C = list(map(lambda x: list(map(int, __import__('__builtin__').raw_input().split())), range(N)))
ans = reduce(add, [min(*pair) for pair in ((C[i][j], C[j][i]) for i in range(N) for j in range(i+1, N))], 0)
print(ans)