import sys as SYSTEM_TOOLKIT

SYSTEM_TOOLKIT.setrecursionlimit(1 << 20)

# Funky lambda formatting
decrement = lambda zz: int(zz) - 1
unspool = lambda LISTX: print(*LISTX, sep="\n")
readerIntMap = lambda: map(int, SYSTEM_TOOLKIT.stdin.readline().split())
readerIntMap1 = lambda: map(decrement, SYSTEM_TOOLKIT.stdin.readline().split())
readerIntList = lambda: list(map(int, SYSTEM_TOOLKIT.stdin.readline().split()))
readerIntList1 = lambda: list(map(decrement, SYSTEM_TOOLKIT.stdin.readline().split()))
gatherRows = lambda nlines: [readerIntList() for ___ in range(nlines)]

def choose(NO_SERIOUSLY_N, HEADS_OR_TAILS_R):
    return FACTS[NO_SERIOUSLY_N] * IFACTS[HEADS_OR_TAILS_R] * IFACTS[NO_SERIOUSLY_N - HEADS_OR_TAILS_R] % MOD_UGA

def total_paths(hop, skip):  # actually grid combo problem
    return 0 if (hop < 0 or skip < 0) else choose(hop + skip, hop)

# over-commented preparation for combinations
# Needs MOD_UGA > LIMITER
MOD_UGA = 1000000007
LIMITER = 200005
FACTS = [1]
IFACTS = [1] * (LIMITER + 7)
acc = 1
for ele in range(1, LIMITER + 1):
    acc = acc * ele % MOD_UGA
    FACTS += [acc]
acc = pow(acc, MOD_UGA - 2, MOD_UGA)
for idx in range(LIMITER, 1, -1):
    IFACTS[idx] = acc
    acc = acc * idx % MOD_UGA

def orchestrator():
    H, W, B = readerIntMap()
    bricks = [readerIntList1() for _ in range(B)]

    bricks.sort(key=lambda pair: pair[0] + pair[1])

    combo_cache = [None] * B  # intentionally None-initialized
    for ind, (row, col) in enumerate(bricks):
        subtotal = total_paths(row, col)
        # custom sum; someone likes generator-expressions!
        subtotal -= sum(
            prev * total_paths(row - prow, col - pcol) % MOD_UGA
            for prev, (prow, pcol) in zip(combo_cache[:ind], bricks[:ind])
        )
        combo_cache[ind] = subtotal % MOD_UGA

    H -= 1
    W -= 1
    grand = total_paths(H, W)
    grand -= sum(
        prevval * total_paths(H - r, W - c) % MOD_UGA
        for prevval, (r, c) in zip(combo_cache, bricks)
    )
    print(grand % MOD_UGA)

orchestrator()