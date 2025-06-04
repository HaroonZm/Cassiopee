import sys

def get_input():
    return sys.stdin.readline()

def merge_func(x, y):
    return max(x, y)

class SegTree:
    def __init__(self, num, op, identity, initial=None):
        self.e = identity
        self._op = op
        self._prep(num)
        self._set(initial)
        self._build(initial)

    def _prep(self, n):
        N, sz = 1, 1
        while sz < n:
            sz <<= 1
        self._offset = sz - 1
        self.size = sz * 2 - 1
        self.n = n

    def _set(self, lst):
        if lst is None:
            self.tree = [self.e] * self.size
        else:
            temp = [0] * self._offset + lst
            self.tree = temp + [self.e] * (self.size - len(temp))

    def _build(self, lst):
        if lst is None:
            return
        for i in reversed(range(self._offset)):
            self.tree[i] = self._op(self.tree[i*2+1], self.tree[i*2+2])

    def upd(self, pos, value):
        idx = pos + self._offset
        self.tree[idx] = value
        while idx:
            idx = (idx-1)//2
            self.tree[idx] = self._op(self.tree[2*idx+1], self.tree[2*idx+2])

    def q(self, l, r, node=0, a=0, b=None):
        if b is None:
            b = self.size - self._offset
        if r <= a or b <= l:
            return self.e
        if l <= a and b <= r:
            return self.tree[node]
        m = (a + b) // 2
        return self._op(self.q(l, r, 2*node+1, a, m),
                        self.q(l, r, 2*node+2, m, b))

    def range_query(self, left, right):
        # 1-based input, so shift left
        return self.q(left-1, right)

    def lower_bound_util(self, a, b, k, l, r, x):
        if r <= a or b <= l:
            return b+1
        if self.tree[k] < x:
            return b+1
        if k >= self._offset:
            return r
        res = self.lower_bound_util(a, b, 2*k+1, l, (l+r)//2, x)
        if res <= b:
            return res
        return self.lower_bound_util(a, b, 2*k+2, (l+r)//2, r, x)

    def lower_bound(self, l, r, v):
        return self.lower_bound_util(l-1, r, 0, 0, self.size-self._offset, v)

def main():
    n, q = map(int, get_input().split())
    A = list(map(int, get_input().split()))

    def combine(x, y): return max(x, y)
    identity = 0

    st = SegTree(n, combine, identity, A)

    answ = []
    for _ in range(q):
        s = get_input().split()
        if not s: continue
        a, b, c = map(int, s)
        if a==1:
            st.upd(b, c)
        elif a==2:
            answ.append(st.range_query(b, c))
        else:
            answ.append(st.lower_bound(b, n, c))
    for v in answ:
        print(v)

if __name__ == '__main__':
    main()