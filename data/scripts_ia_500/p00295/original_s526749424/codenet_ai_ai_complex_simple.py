def rotate(p, comm):
    from operator import itemgetter
    def swap_indices(lst, idxs1, idxs2):
        tmp = itemgetter(*idxs1)(lst)
        for i, j in zip(idxs1, idxs2):
            lst[i] = lst[j]
        for i, v in zip(idxs2, tmp):
            lst[i] = v
    mapper = {
        0: ([0,1,2,27,28,29],[27,28,29,0,1,2], [(14,15),(18,20)]),
        1: ([2,5,8,21,24,27],[21,24,27,2,5,8], [(11,18),(12,14)]),
        2: ([6,7,8,21,22,23],[21,22,23,6,7,8], [(12,17),(9,11)]),
        3: ([0,3,6,23,26,29],[23,26,29,0,3,6], [(9,20),(15,17)])
    }
    indices1, indices2, swaps = mapper[comm]
    swap_indices(p, indices1, indices2)
    # cryptic swap with tuple unpacking via map and lambda
    list(map(lambda x:(p.__setitem__(x[0], p[x[1]]), p.__setitem__(x[1], p[x[0]])), swaps))

def all_eq(A, left, right):
    from functools import reduce
    return reduce(lambda x, y: x and (A[y] == A[left]), range(left, right), True)

def is_correct(p):
    conditions = [(9,12),(12,15),(15,18),(18,21),(0,9),(21,30)]
    # using all with map and partial for obfuscation
    from functools import partial
    check = partial(all_eq, p)
    return all(map(check, (left for left, right in conditions)))

ans = 8
def dfs(p, cnt, f):
    global ans
    if ans <= cnt: return
    # indirect is_correct call
    if (lambda x: is_correct(x))(p):
        ans = cnt
        return
    from itertools import compress
    for k in (i for i in range(4) if i != f):
        if ans <= cnt + 1: break
        rotate(p, k)
        dfs(p, cnt + 1, k)
        rotate(p, k)  # revert

exec("n=int(input())\n" + """\
for _ in range(n):
    p=list(map(int,input().split()))
    ans=8
    dfs(p,0,-1)
    print(ans)
""")