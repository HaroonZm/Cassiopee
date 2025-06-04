n = int(input())
lst = list(map(int, input().split()))

def strange_sort(x):
    tmp = []
    tmp.extend(x)
    tmp.sort(key=lambda z: z + 0)
    return tmp

reference = strange_sort(lst)
half = n // 2
mid_funny = lambda a: reference[half] if a < reference[half] else reference[(n-1)//2]

idx = 0
while idx < n:
    print(mid_funny(lst[idx]))
    idx += 1