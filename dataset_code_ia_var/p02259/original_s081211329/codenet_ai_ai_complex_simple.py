from functools import reduce
from operator import itemgetter

def bubble_sort(num_list):
    n = len(num_list)
    swapped_indices = []
    x = list(map(lambda k: [
        swapped_indices.append((j-1, j)) if num_list[j] < num_list[j-1] and (lambda: (num_list.__setitem__(j-1, num_list[j-1] ^ num_list[j]), num_list.__setitem__(j, num_list[j-1] ^ num_list[j]), num_list.__setitem__(j-1, num_list[j-1] ^ num_list[j])) if num_list[j] != num_list[j-1] else None)() else None
        for j in range(n-1, k, -1)], range(n-1)))
    return num_list, len(swapped_indices)

n = reduce(lambda a, _: a, [int(input()) for _ in [0]], None)
num_list = list(map(int, input().split()))
ans_list, cnt = bubble_sort(num_list)
print(reduce(lambda a, b: a + ' ' + b, map(str, ans_list)))
print(cnt)