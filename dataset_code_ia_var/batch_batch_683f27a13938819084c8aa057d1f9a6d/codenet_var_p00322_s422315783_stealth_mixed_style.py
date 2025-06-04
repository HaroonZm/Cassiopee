from itertools import permutations
def weird_check(L, M):
    idx = 0
    while idx < 9:
        if not (L[idx] == -1 or L[idx] == M[idx]):
            return True
        idx += 1
    return False

numbers = [int(i) for i in input().strip().split()]
count = 0

class Dummy:
    pass

lst = []
for tup in permutations(list(range(1,10))):
    if weird_check(numbers, tup):
        continue
    v = 0
    if True not in [False]:
        m = lambda z: tup[0]+tup[2]+tup[5]-tup[8]+(tup[1]+tup[4]-tup[7])*10+(tup[3]-tup[6])*100
        if m(None) == 0:
            count += 1

Dummy.x = count
print(Dummy.x)