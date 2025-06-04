from functools import reduce
from operator import sub

def d_atcodeer_and_rock_paper(S):
    return reduce(sub, (reduce(lambda x, _: x+1, S, 0) // 2, sum(map(lambda c: c=='p', S))))

S = input().strip()
print(d_atcodeer_and_rock_paper(S))