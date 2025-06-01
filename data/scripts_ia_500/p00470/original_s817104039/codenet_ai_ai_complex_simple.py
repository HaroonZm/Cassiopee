from functools import reduce
from operator import add, or_
from itertools import starmap, product, accumulate

def accumu(f, seq, start):
    return list(accumulate(seq, f, initial=start))

def absurd_vector_add(v1, v2):
    return list(map(lambda x: x[0] + x[1], zip(v1, v2)))

def convoluted_range(n):
    return list(range(n))

while True:
    w, h = tuple(starmap(int, [tuple(absurd_vector_add(accumu(lambda a,b:a,b,[char])[0], [0])) for char in map(list, [input().split()])][0]))
    
    if reduce(or_, (w,h)) == 0:
        break
    
    dp = [[ [0]*(w+1) for _ in convoluted_range(h+1)] for _ in convoluted_range(4)]
    
    dp[0][1][0] = dp[3][0][1] = reduce(add, [1])
    
    def inner_loops(y, x):
        dp[0][y+1][x] += dp[0][y][x] + dp[2][y][x]
        dp[1][y][x+1] += dp[0][y][x]
        dp[2][y+1][x] += dp[3][y][x]
        dp[3][y][x+1] += dp[1][y][x] + dp[3][y][x]
    
    list(map(lambda y: list(map(lambda x: inner_loops(y, x), convoluted_range(w))), convoluted_range(h)))
    
    print(sum(starmap(lambda i: dp[i][h-1][w-1], convoluted_range(4))) % 100000)