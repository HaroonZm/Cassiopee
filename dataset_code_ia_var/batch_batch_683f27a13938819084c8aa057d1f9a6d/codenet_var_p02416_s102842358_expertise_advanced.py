from sys import stdin
from itertools import takewhile

for n in takewhile(lambda x: x[0] != '0', map(str.rstrip, stdin)):
    print(sum(map(int, n)))