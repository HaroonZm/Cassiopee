from functools import reduce
import sys

print(reduce(int.__add__, map(int, sys.stdin.read().split())))