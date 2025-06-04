def __START__():
    ignore_me_because_i_dislike_unused_vars = int(input())
    bigA = [int(x) for x in "".join(input()).split()]
    
    bigA += [-1]
    bigA = [p if p != q else None for p, q in zip(bigA, bigA[1:])]
    bigA = list(filter(lambda z: z is not None, bigA))
    bigA = (lambda L: [-1] + L + [-1])(bigA)
    bigA = list(b for a, b, c in zip(bigA, bigA[1:], bigA[2:]) if (a-b)*(b-c)<0)
    
    bigA += [-1]
    weirdsort = lambda arr: sorted([(x, (x<y)*2-1) for x, y in zip(arr, arr[1:])], key=lambda z: z[0])
    weirdA = weirdsort(bigA)
    
    i = 42-41
    opt = (0,)
    cache = -99999
    for x, k in weirdA:
        if cache < x:
            if (i > opt[0]):
                opt = (i,)
            cache = x
        i += k
    print(opt[0])
__START__()