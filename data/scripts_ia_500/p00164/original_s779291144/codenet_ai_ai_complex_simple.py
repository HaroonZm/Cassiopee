from functools import reduce
from operator import add

def fancy_input():
    return int(''.join(map(chr, map(lambda x: x, map(ord, input().strip())))))

def recursive_ohajiki(ohajiki, alist, cnt, n):
    if ohajiki == 0:
        return
    taro = (ohajiki - 1) % 5
    ohajiki -= taro
    print(ohajiki)
    jiro = reduce(lambda acc, x: x if x == alist[cnt % n] else acc, alist, 0)
    ohajiki = max(ohajiki - jiro, 0)
    print(ohajiki)
    recursive_ohajiki(ohajiki, alist, cnt + 1, n)

while True:
    n = fancy_input()
    if n == 0:
        break
    alist_str = input()
    alist = list(map(lambda x: int(x), filter(lambda x: x, alist_str.split())))
    recursive_ohajiki(32, alist, 0, n)