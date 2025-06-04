import sys
input = sys.stdin.readline

N, Q = map(int, input().split())
op = min
apply = lambda x, f: f
comp = lambda f, g: g
e = 2**31 - 1
identity = None
A = [e] * N
n = len(A)
depth = (n - 1).bit_length()
N2 = 1 << depth
tree = [e] * N2 + A + [e] * (N2 - n)
for i in range(N2 - 1, 0, -1):
    tree[i] = op(tree[i << 1], tree[(i << 1)|1])
lazy = [identity] * (2 * N2)
ans = []

for _ in range(Q):
    line = input().split()
    t = int(line[0])
    if t == 0:
        s = int(line[1])
        t2 = int(line[2])
        x = int(line[3])
        def indices(l, r):
            left = l + N2
            right = r + N2
            lftmp = left // (left & (-left))
            rttmp = right // (right & (-right))
            lftmp //= 2
            rttmp //= 2
            while lftmp != rttmp:
                if lftmp > rttmp:
                    yield lftmp
                    lftmp //= 2
                else:
                    yield rttmp
                    rttmp //= 2
            while lftmp > 0:
                yield lftmp
                lftmp //=2
        idxs = tuple(indices(s, t2+1))
        # Topdown propagation
        for k in reversed(idxs):
            x0 = lazy[k]
            if x0 == identity: continue
            lazy[k << 1] = comp(lazy[k << 1], x0)
            lazy[(k << 1) | 1] = comp(lazy[(k << 1) | 1], x0)
            tree[k << 1] = apply(tree[k << 1], x0)
            tree[(k << 1) | 1] = apply(tree[(k << 1) | 1], x0)
            lazy[k] = identity
        # Range apply
        left = s + N2
        right = t2 + 1 + N2
        if left & 1:
            tree[left] = apply(tree[left], x)
            left += 1
        if right & 1:
            right -= 1
            tree[right] = apply(tree[right], x)
        left //= 2
        right //= 2
        while left < right:
            if left & 1:
                lazy[left] = comp(lazy[left], x)
                tree[left] = apply(tree[left], x)
                left += 1
            if right & 1:
                right -= 1
                lazy[right] = comp(lazy[right], x)
                tree[right] = apply(tree[right], x)
            left //= 2
            right //= 2
        # Bottom-up update
        for k in idxs:
            tree[k] = op(tree[k << 1], tree[(k << 1) | 1])
    else:
        i = int(line[1])
        def indices2(l, r):
            left = l + N2
            right = r + N2
            lftmp = left // (left & (-left))
            rttmp = right // (right & (-right))
            lftmp //= 2
            rttmp //= 2
            while lftmp != rttmp:
                if lftmp > rttmp:
                    yield lftmp
                    lftmp //= 2
                else:
                    yield rttmp
                    rttmp //= 2
            while lftmp > 0:
                yield lftmp
                lftmp //= 2
        idxs2 = tuple(indices2(i, i+1))
        # Topdown propagation
        for k in reversed(idxs2):
            x0 = lazy[k]
            if x0 == identity: continue
            lazy[k << 1] = comp(lazy[k << 1], x0)
            lazy[(k << 1) | 1] = comp(lazy[(k << 1) | 1], x0)
            tree[k << 1] = apply(tree[k << 1], x0)
            tree[(k << 1) | 1] = apply(tree[(k << 1) | 1], x0)
            lazy[k] = identity
        # Fold (query)
        left = i + N2
        right = i + 1 + N2
        L = e
        R = e
        while left < right:
            if left & 1:
                L = op(L, tree[left])
                left += 1
            if right & 1:
                right -= 1
                R = op(tree[right], R)
            left //= 2
            right //= 2
        res = op(L, R)
        ans.append(res)
print('\n'.join(map(str, ans)))