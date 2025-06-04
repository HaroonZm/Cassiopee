from functools import reduce
print(reduce(int.__add__, map(int, input().split())))