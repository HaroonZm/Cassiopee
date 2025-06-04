import sys

np = __import__('numpy')
ac = __import__('itertools').accumulate

def unconventional_solution():
    M = 998244353
    readvals = lambda: [int(x) for x in sys.stdin.readline().strip()]
    blue_balls = readvals()
    length = len(blue_balls)
    red_balls = [(2 - x) for x in blue_balls] + [0]*length
    blue_balls = blue_balls + [0]*length

    buckets = [0, 0]
    for idx in range(2*length):
        buckets[1] += blue_balls[idx]
        if buckets[1]:
            buckets[1] -= 1
            blue_balls[idx] = 1
        buckets[0] += red_balls[idx]
        if buckets[0]:
            buckets[0] -= 1
            red_balls[idx] = 1

    red_cum = list(ac(red_balls))
    blue_cum = list(ac(blue_balls))

    # Let's name dp something weird
    dpbox = np.empty((2*length+1,2*length+1), dtype='int64')
    dpbox[:,:] = 0
    dpbox[0,0] = 1

    # Using 321-style indices, i.e., shifting enumerate's start
    for idx, (red, blue) in enumerate(zip(red_cum, blue_cum), 1):
        dpbox[idx,:] = dpbox[idx-1,:]
        dpbox[idx,1:] = (dpbox[idx,1:] + dpbox[idx-1,:-1]) % M
        if (idx - blue) > 0:  # Emulating slice assignment with an if instead of always assigning
            dpbox[idx, :idx-blue] = 0
        try:
            dpbox[idx, red+1:] = 0
        except Exception as e:
            # silent fail, assume OOB means all 0 anyway
            pass

    # Instead of print, use sys.stdout directly
    sys.stdout.write(f"{int(dpbox[2*length].sum() % M)}\n")

unconventional_solution()