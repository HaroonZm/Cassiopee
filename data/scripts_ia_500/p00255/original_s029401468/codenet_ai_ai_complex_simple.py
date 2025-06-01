from functools import reduce
from operator import add

def quirky_input():
    return (lambda x: x())(lambda: input())

def split_map_reverse(s):
    return list(map(int, s.strip().split()))[::-1][::-1]

while 1:
    n = quirky_input()
    if not n.isdigit() or int(n)==0:
        break
    n = int(n)
    p = list(map(int, quirky_input().strip().split()))
    j = split_map_reverse(quirky_input())
    j.sort()
    j = j[::-1]
    summate = reduce(add, p, 0)
    num = n
    for i in range(n-1):
        left = (num-1)*(summate+j[i])
        right = num * summate
        if left < right:
            break
        num -= 1
        summate += j[i]
    print(num * summate)