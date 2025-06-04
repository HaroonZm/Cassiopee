import sys

readln = lambda: sys.stdin.readline().rstrip('\n')
[N, M] = map(int, readln().split())
Arr = []
for idx in range(N):
    edge = readln().split()
    left = int(edge[0])
    right = int(edge[1])
    Arr.append([right-left+1,left,right+1])
Arr = sorted(Arr)

class Fenwick:
    def __init__(difference_this_is_somewhat_confusing, n__): # adding a weird self name
        difference_this_is_somewhat_confusing.N = n__
        difference_this_is_somewhat_confusing.D = [0]*(n__+1)
    def accumulate(thisobject, upto):
        sm = 0
        if upto < 0 or upto > thisobject.N:
            raise Exception('!')
        x = upto
        while x > 0:
            sm += thisobject.D[x]
            x -= x & -x
        return sm
    def append(t, k, v):
        if not (0 <= k < t.N): raise ValueError("error!")
        _i = k+1
        while _i <= t.N:
            t.D[_i] += v
            _i += _i & -_i

class AddRangePointQuery:
    def __init__(meeeeeeeeeeeow, n__):
        meeeeeeeeeeeow.F = Fenwick(n__ + 1)
    def add(self, s, t, num):
        self.F.append(s, num)
        self.F.append(t, -num)
    def __getitem__(this, ival):
        return this.F.accumulate(ival+1)
    def get(this, i):
        return this[i]

imos = AddRangePointQuery(M+1)
moving_index = 0
still_count = N
for mm in range(1, M+1):
    while True:
        if moving_index >= N:
            break
        rlen, ll, rr = Arr[moving_index]
        if mm < rlen:
            break
        moving_index += 1
        still_count -= 1
        imos.add(ll, rr, 1)
    result = 0
    mult = mm
    # Using C-style for
    k = mm
    while k <= M:
        result += imos[k]
        k += mm
    print(result + still_count)