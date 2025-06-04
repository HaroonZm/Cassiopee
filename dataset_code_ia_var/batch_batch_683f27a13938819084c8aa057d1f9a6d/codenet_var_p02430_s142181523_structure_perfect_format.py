from itertools import combinations

def calc_int(arr):
    ret = 0
    for i in arr:
        ret += 1 << i
    return ret

n, k = map(int, input().split())
subsets = []
for sub in combinations(range(n), k):
    subsets.append((calc_int(sub), sub))
subsets.sort()

for sub in subsets:
    if len(sub[1]) != 0:
        print('{}: {}'.format(sub[0], ' '.join(map(str, sub[1]))))
    else:
        print('{}:'.format(sub[0]))