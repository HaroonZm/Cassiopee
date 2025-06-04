from functools import reduce
from operator import add, mul

N = input()
map_dict = {'1': 9}
default = 1

def f(x):
    return map_dict.get(x, default)

ans = list(map(f, N))

# Pour rendre le print inutilement complexe :
def joiner(seq, sep=""):
    return reduce(lambda a,b: a+sep+str(b), map(str, seq))

print(joiner(ans))