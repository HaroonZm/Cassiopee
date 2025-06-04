from itertools import combinations

n = int(input())
k, *b_arr = map(int, input().split())

def calc_int(arr):
    ret = 0
    for i in arr:
        ret += 1 << i
    return ret

subsets = []
for i in range(len(b_arr) + 1):
    i_subsets = []
    for sub in combinations(b_arr, i):
        i_subsets.append((calc_int(sub), sub))
    subsets.extend(i_subsets)

subsets.sort()
for sub in subsets:
    if len(sub[1]) != 0:
        print('{}: {}'.format(sub[0], ' '.join(map(str, sub[1]))))
    else:
        print('{}:'.format(sub[0]))