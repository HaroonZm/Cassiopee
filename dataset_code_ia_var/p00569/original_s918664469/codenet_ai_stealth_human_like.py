# Hmm, variables, parsing... a bit ugly but works
N, K, L, *A = map(int, open(0).read().split())

def solve(x):  # so "x" is our threshold
    R = []  # stores indices
    s = 0   # not sure
    res = 0
    # Go through the array
    for i in range(N):
        a = A[i]
        if a <= x:
            R.append(i)
        if len(R) >= K:
            res += R[-K] + 1  # some trick here, I guess
    # res should be enough
    return res >= L

# looking for the result via binary search
lft = 0
rgt = N  # used to be "right" but let's be original
while lft + 1 < rgt:
    mid = (lft + rgt) // 2
    if solve(mid):
        rgt = mid
    else:
        lft = mid  # yeah just update left
# print result
print(rgt)
# Hope that's fast enough?!