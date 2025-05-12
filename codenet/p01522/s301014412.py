n, k = map(int, raw_input().split())
bunny = [0] * 51
bad = [False] * 51
for i in xrange(k):
    nums = map(int, raw_input().split())[1:]
    for nu in nums:
        bunny[nu] = i
for i in xrange(input()):
    p, q = map(int, raw_input().split())
    if bunny[p]==bunny[q]:
        bad[p] = bad[q] = True
print bad.count(True)