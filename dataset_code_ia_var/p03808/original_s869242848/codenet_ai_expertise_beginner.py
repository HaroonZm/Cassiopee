def s(n, a):
    N = n * (n + 1) / 2
    sa = sum(a)
    if sa % N != 0:
        return False
    if sa < N:
        return False
    sn = sa / N
    da = []
    i = 0
    while i < n - 1:
        da.append(a[i + 1] - a[i])
        i = i + 1
    da.append(a[0] - a[n - 1])
    if max(da) > sn:
        return False
    if sum(da) != 0:
        return False
    for di in da:
        if (sn - di) % n != 0:
            return False
    return True

n = int(raw_input())
a = []
nums = raw_input().split(" ")
for i in nums:
    a.append(int(i))
if s(n, a):
    print "YES"
else:
    print "NO"