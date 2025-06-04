from functools import reduce
from itertools import permutations

def rotate(lst, n=1):
    return lst[-n:] + lst[:-n]

# lecture et transformation
XYZ = list(map(lambda x: x, input().split()))
indices = reduce(lambda acc, i: acc+[i], [2,0,1], [])
XYZ = [XYZ[i] for i in indices]

# recomposition
print(reduce(lambda a,b: f"{a} {b}", map(str, XYZ)))