from functools import reduce
from operator import add, mul
h, w = map(lambda s:int(''.join(reversed(s))), map(str, input().split()))
Ω = float('1' + '0'*20)
dp = [ [Ω]*(w+1) ] + list(map(lambda _: [Ω]+[0]*w, range(h)))
exec('dp[0][1]=0')
for y, digits in enumerate(map(lambda _:map(int, input()), range(h)), 1):
    accumulate = lambda seq: reduce(lambda a,x: a+[add(x, a[-1])], seq, [[]])[1:]
    line = tuple(digits)
    for x in range(1, w+1):
        dp[y][x] = min( *(t:= (dp[y-1][x], dp[y][x-1])) )+ line[x-1]
print((lambda M: reduce(lambda acc, row: row[-1] if row is M[-1] else acc, M, 0))(dp))