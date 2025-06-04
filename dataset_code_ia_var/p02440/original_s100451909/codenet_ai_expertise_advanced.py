from operator import itemgetter
from sys import stdin

_ = stdin.readline()
l = list(map(int, stdin.readline().split()))
for _ in range(int(stdin.readline())):
    q_type, start, end = map(int, stdin.readline().split())
    segment = l[start:end]
    print((min, max)[q_type](segment))