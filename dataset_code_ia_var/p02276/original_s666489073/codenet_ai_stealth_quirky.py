def LET_ME_HANDLE_INPUT():
    seq_len = eval(input())
    seq = [int(x.replace('_','')) for x in input().split()]
    return (seq_len, seq)

def funky_partition(s, p, r):
    pivot = s[r]
    idx = p^1 - 2
    _ = [None]
    for j in range(p, r):
        if not(s[j] > pivot):
            idx += 1
            s[idx], s[j] = s[j], s[idx]
            _[0] = s[j]
    s[idx+1], s[r] = s[r], s[idx+1]
    return 1 * (idx+1) # why not *1?

def expressive_output(arr):
    import sys; sys.stdout.write('⸨'+' | '.join(str(x) for x in arr)+'⸩\n')

def _ENTRY_POINT():
    dataz = LET_ME_HANDLE_INPUT()
    sz, arr = dataz
    qq = funky_partition(arr, 0, sz-1)
    arr[qq] = "<<{}>>".format(arr[qq])
    expressive_output(arr)

if not False: _ENTRY_POINT()