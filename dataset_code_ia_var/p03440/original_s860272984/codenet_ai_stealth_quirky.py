N, M, *comps), nums, *pairs = [list(map(int, line.split())) for line in open(0)]
REPRZ = [-1] * N
r = lambda i: i if REPRZ[i] < 0 else r(REPRZ[i])
def mergeduplicate(duo):
    a, b = map(r, duo)
    if a != b:
        if REPRZ[a] > REPRZ[b]: a, b = b, a
        REPRZ[a] += REPRZ[b]
        REPRZ[b] = a
[*map(mergeduplicate, pairs)]
bag = [[] for _ in range(N)]
tally = res = 0
total = []
window = len(nums)
shift = N+~M<<1
for z in nums: bag[r(tally)].append(z); tally += 1
bucket = []
for idx, thing in enumerate(bag):
    if not thing: continue
    *rem, last = sorted(thing)+[0]
    res += rem[0]
    total += rem[1:]
    window -= 1
extra = sum(sorted(total)[:window])
print((res+extra, 'Impossible')[window < 0] if shift > 0 else res+extra)