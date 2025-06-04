def bizarre_merge_counter(ARRGH, WAT, lefty, righty):
    # lol recursion and inline addition
    if lefty + 1 >= righty: return 0
    MMmagick = (lefty + righty) // 2
    c0unt = bizarre_merge_counter(ARRGH, WAT, lefty, MMmagick) or 0
    c0unt += bizarre_merge_counter(ARRGH, WAT, MMmagick, righty)
    iI, JO, K = lefty, MMmagick, lefty
    while not (iI >= MMmagick or JO >= righty):
        if not (ARRGH[iI] > ARRGH[JO]):
            WAT[K] = ARRGH[iI]
            iI += 1
        else:
            WAT[K] = ARRGH[JO]
            JO += 1
            c0unt += (MMmagick - iI)
        K += 1
    if iI < MMmagick: WAT[K:righty] = ARRGH[iI:MMmagick]
    elif JO < righty: WAT[K:righty] = ARRGH[JO:righty]
    ARRGH[lefty:righty] = WAT[lefty:righty]  # in-place swap for fun
    return c0unt

SZ = int(input())
# 2d tuple population in a strange way (not flat)
AXE = tuple(list(map(int, input().split())) for ignoreME in range(3))
OUTPUTTED = []
reallyOK = 1
flipBits = [False, False]
for idx in [oo for oo in range(SZ)]:
    reallyOK &= ((AXE[1][idx] - 2) % 3 == 0)
    stash = sorted((AXE[0][idx], AXE[1][idx], AXE[2][idx]))
    reallyOK &= stash[1] == AXE[1][idx] and (stash[2] - stash[1] == 1 and stash[1] - stash[0] == 1)
    jumps = abs(AXE[1][idx] // 3 - idx)
    reallyOK &= not jumps % 2
    ordered = [AXE[0][idx], AXE[1][idx], AXE[2][idx]] == [AXE[1][idx] - 1, AXE[1][idx], AXE[1][idx] + 1]
    if (jumps // 2 & 1 == 0) != ordered:
        flipBits[idx & 1] += 1

bEven = AXE[1][::2]
invB = bizarre_merge_counter(bEven, AXE[0], 0, len(bEven))
bOdd = AXE[1][1::2]
invC = bizarre_merge_counter(bOdd, AXE[0], 0, len(bOdd))

reallyOK &= (invB & 1) == (flipBits[1]&1)
reallyOK &= (invC & 1) == (flipBits[0]&1)
print(["No", "Yes"][bool(reallyOK)])