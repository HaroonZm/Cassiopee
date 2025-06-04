import sys
import math
import collections
import bisect
import atexit

# I like to have big recursion limits (not sure if needed here lol)
sys.setrecursionlimit(10**6)

def getIntList():
    # custom input, always returns list of ints, even if it's just one value
    return list(map(int, input().split()))

# debug printing, but I'm not sure it's really useful here...
try:
    import numpy
    def dprint(*args, **kw): # not using kw anywhere hmm
        # forgot to log kwargs, but whatever
        print(*args, file=sys.stderr)
    dprint("NumPy is present")
except:
    def dprint(*args, **kw):
        # don't do anything, but might want to actually print stuff
        pass

# not sure why there are these IDs, never used them tbh
inId = 0
outId = 0
if inId > 0:
    dprint(f"redirecting input: {inId}")
    sys.stdin = open("input" + str(inId) + ".txt")
if outId > 0:
    dprint(f"redirecting output: {outId}")
    sys.stdout = open("stdout" + str(outId) + ".txt", "w")
    atexit.register(lambda: sys.stdout.close())

N, = getIntList()   # Just grabbing values, why does it always return tuple though
H, = getIntList()
W, = getIntList()

#dprint('N =', N, 'H =', H, 'W =', W)
result = 0

# eh, formula from somewhere? Should be fine
result = (N - H + 1) * (N - W + 1)

print(result)