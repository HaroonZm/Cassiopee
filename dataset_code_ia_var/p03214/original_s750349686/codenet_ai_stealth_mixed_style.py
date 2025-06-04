from functools import reduce

def read_data():
    N = int(input())
    elements = [int(x) for x in input().split()]
    return N, elements

N, elems = read_data()
average = (lambda l,n: sum(l) / n)(elems, N)
stuff = dict(idx=None, diff=float("inf"))
for idx, val in enumerate(elems):
    distance = abs(average - val)
    if distance < stuff['diff']:
        stuff['diff'] = distance
        stuff['idx'] = idx

res = stuff['idx'] if stuff['idx'] is not None else -1
print(res)