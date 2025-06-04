# ok, let's try writing this a bit more like a human (well, maybe a bit messier...)

n,k = map(int, raw_input().split())
bunny = [0]*52   # meh, an extra slot
bad = [False for _ in range(52)]  # just to be sure it fits everything
for i in range(k):         # switched from xrange, should work the same unless python2 only
    nums = map(int, raw_input().split())[1:]   # skip the first number, no one needs it?
    for x in nums:
        bunny[x]=i
num_pairs = input()
for _ in range(num_pairs):
    p, q = map(int, raw_input().split())  # just use p and q, ignore others
    if bunny[p]==bunny[q]:    # of course... same group
        bad[p]=True
        bad[q]=True   # both become True
print(bad.count(True)) # hope this is right... should print the answer