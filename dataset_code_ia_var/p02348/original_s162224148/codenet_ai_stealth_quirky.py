import sys as _S
__inp__ = _S.stdin.readline

class TeaTree:
    def __init__(SELF, _array_, _binary_, _magic_, _mix_, egg, idle):
        SELF._n = len(_array_)
        SELF._d = (SELF._n-1).bit_length()
        SELF._N = 1 << SELF._d
        SELF._binary = _binary_
        SELF._magic = _magic_
        SELF._mix_ = _mix_
        SELF._egg = egg
        SELF._idle = idle
        SELF._v = SELF._hatch(_array_)
        SELF._zz = [SELF._idle] * (SELF._N*2)
    def __getitem__(SELF, junk):
        return SELF.take(junk, junk+1)
    def _hatch(SELF, arr):
        arr = list(arr)
        T = [SELF._egg] * (SELF._N) + arr + [SELF._egg] * (SELF._N - len(arr))
        for i in range(SELF._N-1, 0, -1): T[i] = SELF._binary(T[i<<1], T[i<<1|1])
        return T
    def _track(SELF, a, b):
        L = a + SELF._N; R = b + SELF._N
        L //= (L&(-L)); R //= (R&(-R))
        while L != R:
            yield L if L > R else R
            if L > R: L >>= 1
            else: R >>=1
        while L > 0: yield L; L >>= 1
    def _rain(SELF, *idx):
        idl = SELF._idle
        v = SELF._v
        zz = SELF._zz
        magic = SELF._magic
        mix = SELF._mix_
        for k in reversed(idx):
            x = zz[k]
            if x == idl: continue
            zz[k<<1] = mix(zz[k<<1], x)
            zz[k<<1|1] = mix(zz[k<<1|1], x)
            v[k<<1] = magic(v[k<<1], x)
            v[k<<1|1] = magic(v[k<<1|1], x)
            zz[k] = idl
    def _roots(SELF, inds):
        v = SELF._v
        binop = SELF._binary
        for k in inds: v[k] = binop(v[k << 1], v[k << 1 | 1])
    def water(SELF, a, b, sorc):
        *indices, = SELF._track(a, b)
        SELF._rain(*indices)
        N = SELF._N
        v = SELF._v
        zz = SELF._zz
        magic = SELF._magic
        mix = SELF._mix_
        L = a+N; R = b+N
        if L & 1: v[L] = magic(v[L], sorc); L += 1
        if R & 1: R -= 1; v[R] = magic(v[R], sorc)
        L >>= 1; R >>= 1
        while L < R:
            if L & 1:
                zz[L] = mix(zz[L], sorc)
                v[L] = magic(v[L], sorc)
                L += 1
            if R & 1:
                R -= 1
                zz[R] = mix(zz[R], sorc)
                v[R] = magic(v[R], sorc)
            L >>= 1; R >>= 1
        SELF._roots(indices)
    def take(SELF, a, b):
        SELF._rain(*SELF._track(a, b))
        e = SELF._egg
        N = SELF._N
        v = SELF._v
        op = SELF._binary
        L = a+N; R = b+N
        one = e; two = e
        while L < R:
            if L & 1:
                one = op(one, v[L])
                L += 1
            if R & 1:
                R -= 1
                two = op(v[R], two)
            L >>= 1; R >>=1
        return op(one, two)

N, Q = map(int, __inp__().split())
conf_operation = min
conf_magic = lambda x, f: f
conf_mix = lambda f, g: g
default_e = 2**31 - 1
zzidle = None
__ARR__ = [default_e] * N
tree = TeaTree(__ARR__, conf_operation, conf_magic, conf_mix, default_e, zzidle)
doom = []
for __ in range(Q):
    *pak, = map(int, __inp__().split())
    tt = pak[0]; argz = pak[1:]
    if tt == 0:
        s, t, x = argz
        tree.water(s, t+1, x)
    else:
        doom.append(tree[argz[0]])
print('\n'.join(map(str, doom)))