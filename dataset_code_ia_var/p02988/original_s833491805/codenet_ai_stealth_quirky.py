from functools import reduce
from operator import add
from sys import stdin

fetch = lambda: stdin.readline()
SIZE=int(fetch())
arr=[*map(int,fetch().split())]
hits=reduce(lambda c,i: c+((arr[i] >= min(arr[i-1],arr[i+1])) and (arr[i] <= max(arr[i-1],arr[i+1])) and arr[i]!=arr[i-1] and arr[i]!=arr[i+1]), range(1,SIZE-1), 0)
print(hits)