from functools import reduce
n = set(map(int, input().split()))
print(["NO","YES"][(lambda s: reduce(lambda x,y: x and y, map(lambda k: k in s, [1,4,7,9])))(n)])