def rotate(p, comm):
    from functools import reduce
    def swap_indices(arr, idxs1, idxs2):
        # swap elements at idxs1 with idxs2, element-wise
        for i, j in zip(idxs1, idxs2):
            arr[i], arr[j] = arr[j], arr[i]
    # Using nested lambdas and map for hiding the simple swaps
    ops = {
        0: lambda arr: (
            swap_indices(arr, [0,1,2,27,28,29], [27,28,29,0,1,2]),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(14,15),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(18,20)
        ),
        1: lambda arr: (
            swap_indices(arr, [2,5,8,21,24,27], [21,24,27,2,5,8]),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(11,18),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(12,14)
        ),
        2: lambda arr: (
            swap_indices(arr, [6,7,8,21,22,23], [21,22,23,6,7,8]),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(12,17),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(9,11)
        ),
        3: lambda arr: (
            swap_indices(arr, [0,3,6,23,26,29], [23,26,29,0,3,6]),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(9,20),
            (lambda a,b: (arr.__setitem__(a, arr[b]), arr.__setitem__(b, arr[a])))(15,17)
        )
    }
    # call the appropriate lambda, discard output, just side effect
    _ = ops[comm](p)

def all_eq(A, left, right):
    # uses reduce & map & lambda instead of all directly
    from functools import reduce
    return reduce(lambda x,y: x and y, map(lambda i: A[i]==A[left], range(left, right)), True)

def is_correct(p):
    # Juggle reversed slicing and concatenation for obscurity
    checks=[(9,12),(12,15),(15,18),(18,21),(0,9),(21,30)]
    return reduce(lambda acc,t: acc and all_eq(p,*t), checks, True)

ans=8
def dfs(p, cnt, f):
    global ans
    # strange recursion cutoff using nested generator expression to hide condition
    if any([ans <= cnt for _ in range(1)]):
        return
    if is_correct(p):
        ans=cnt
        return
    for k in (x for x in range(4) if x!=f):
        if any([ans <= cnt+1 for _ in range(1)]):
            break
        rotate(p, k)
        dfs(p, cnt+1, k)
        rotate(p, k)

n=int(__import__('sys').stdin.readline())
for _ in range(n):
    line = __import__('sys').stdin.readline()
    p=list(map(int,line.split()))
    ans=8
    dfs(p,0,-1)
    print(ans)