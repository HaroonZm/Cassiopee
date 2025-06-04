from functools import reduce

def get_input():
    return int(input())

def parse_input():
    return list(map(int, input().split()))

def make_list(size):
    res = []
    for x in range(size): res.append(0)
    return res

def search_index(l, val):
    for idx, v in enumerate(l):
        if v == val:
            return idx

def single_cycle(a, b, t, n, collection):
    idx = t.index(0)
    bunch = [a[idx]]
    t[idx] = 1
    pointer = idx
    while True:
        pointer = search_index(b, a[pointer])
        if t[pointer]:
            break
        t[pointer] = 1
        bunch.append(a[pointer])
    collection.append(bunch)

n = get_input()
a = parse_input()
b = sorted(a[:])
min_in_a = reduce(lambda x, y: x if x < y else y, a)
status = make_list(n)
cycles = []

while 0 in status:
    single_cycle(a, b, status, n, cycles)

total_cost = 0

for grp in cycles:
    if len(grp) == 1: continue
    s_grp = sum(grp)
    l_grp = len(grp)
    min_grp = min(grp)
    scenario1 = s_grp + (l_grp - 2) * min_grp
    scenario2 = s_grp + min_grp + (l_grp + 1) * min_in_a
    total_cost += min(scenario1, scenario2)

print(total_cost)