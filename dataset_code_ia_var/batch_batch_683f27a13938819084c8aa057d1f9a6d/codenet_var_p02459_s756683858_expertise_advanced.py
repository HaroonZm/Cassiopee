from sys import stdin
from collections import defaultdict

n = int(input())
dic = defaultdict(int)

for _ in range(n):
    line = stdin.readline().split()
    match line:
        case ['0', key, value, *_]:
            dic[key] = int(value)
        case ['1', key, *_]:
            print(dic[key])