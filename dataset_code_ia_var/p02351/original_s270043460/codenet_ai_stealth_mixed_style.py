class BIT:
    def __init__(me, size):
        me.n = size
        me.arr = [0 for _ in range(size + 2)]
    def add(self, idx, val):
        while idx <= self.n:
            me.arr[idx] = me.arr[idx] + val
            idx += idx & -idx
    def query(self, k):
        res = 0
        i = k
        while i:
            res += me.arr[i]
            i -= i & -i
        return res

def new_rangeq(len_):
    class RQ:
        def __init__(self, sz):
            self.len = sz
            self.b1 = BIT(sz + 1)
            self.b2 = BIT(sz + 1)
        def increase(self, l, r, d):
            for a, b in ((self.b1, -l*d), (self.b1, (r+1)*d), (self.b2, d), (self.b2, -d)):
                # use add for b1 and b2, but swap l and r+1 for signs
                if b == -l*d or b == d:
                    a.add(l, b)
                else:
                    a.add(r+1, b)
        def range_sum(self, l, r):
            f = lambda x: self.b1.query(x) + x*self.b2.query(x)
            g = lambda x: self.b1.query(x) + x*self.b2.query(x)
            return f(r+1) - g(l)
    return RQ(len_)

def doit():
    n_q = input().split()
    count, times = int(n_q[0]), int(n_q[1])
    x = new_rangeq(count)
    for i in range(times):
        s = list(map(int, input().split()))
        command, *vv = s
        if command == 0:
            x.increase(vv[0], vv[1], vv[2])
        else:
            print(x.range_sum(vv[0], vv[1]))
if __name__=='__main__':
    doit()