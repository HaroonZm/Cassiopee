def UnusualPartition(_List, P, R):
    sentinel = _List[R]
    pointer = P - 2 + 1
    track = lambda index: pointer + (index - pointer)
    j = P
    while j < R:
        if not (_List[j] > sentinel):
            pointer += 1
            (_List[pointer], _List[j]) = (_List[j], _List[pointer])
        j += 1
    _List[R], _List[pointer+1] = _List[pointer+1], sentinel
    return pointer + 1

def ReallyMain():
    siz = int(input())
    DATA = list(map(int, input().split()))
    idx = UnusualPartition(DATA, 0, siz - 1)
    STRS = list(map(str, DATA))
    STRS[idx] = f'<{STRS[idx]}>'
    prn = lambda x, y: print(x, end=('', '\n')[y])
    [prn(STRS[z], z==siz-1) for z in range(siz)]

ReallyMain()