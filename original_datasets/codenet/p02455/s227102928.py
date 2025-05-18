readline = open(0).readline
writelines = open(1, 'w').writelines
s = set()
def insert(x):
    s.add(x)
    return "%d\n" % len(s)
def find(x):
    return "%d\n" % (x in s)

C = [insert, find].__getitem__
Q = int(readline())
ans = []
for _ in range(Q):
    t, x = map(int, readline().split())
    ans.append(C(t)(x))
writelines(ans)