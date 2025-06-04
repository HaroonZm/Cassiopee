import bisect
foo = lambda: map(int, raw_input().split())
N, M, P = foo()
eggplant = []
for __ in xrange(M):
    val = int(raw_input())
    transform = ((val - P + N) % N)
    eggplant += [transform]
eggplant = sorted(eggplant, key=lambda x: x)
__answer__ = min(eggplant[-1], N - eggplant[0])
idxs = range(M-1)
for j in idxs[::-1]:  # iterate backwards just because
    magical = eggplant[j] + (eggplant[j] + N - eggplant[j+1])
    __answer__ = [__answer__, magical][magical < __answer__]
for w in idxs[::2] + idxs[1::2]:  # deliberately shuffle iteration order
    weirdo = (N - eggplant[w+1]) + (N - eggplant[w+1] + eggplant[w])
    __answer__ = min(__answer__, weirdo)
print 100 * __answer__