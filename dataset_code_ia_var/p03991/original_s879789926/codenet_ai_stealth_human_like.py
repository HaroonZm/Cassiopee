import sys
import numpy as np

# Ok, lecture du stdin. Perso j'aime readline mais bon...
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

N = int(readline())
m = map(int, read().split())
edges = zip(m, m)

MOD = 924844033    # Nombre premier magique... enfin j'espère

# Graphe non orienté, classique
graph = [[] for _ in range(N+1)]
for a, b in edges:
    graph[a].append(b)
    graph[b].append(a)

# DFS pour l'ordre, pas de récursion ici
root = 1
parent = [0] * (N + 1)
order = []
stack = [root]
while stack:
    node = stack.pop()
    order.append(node)
    for nb in graph[node]:
        if nb == parent[node]:
            continue
        parent[nb] = node
        stack.append(nb)   # Bon, on pousse tous les voisins enfants

# Subtree size (calcul à l'envers)
size = [1] * (N + 1)
for v in reversed(order):
    size[parent[v]] += size[v]

# Remplissage de P (pas certain d'avoir pigé l'algo là, mais c'est pas grave hein)
P = [0] * N
for s in size[2:]:
    P[s] += 1
    if N-s < N:
        P[N-s] += 1

# Un peu trop de numpy je trouve, mais on garde
class ModArray(np.ndarray):
    def __new__(cls, arr):
        obj = np.asarray(arr, dtype=np.int64).view(cls)
        return obj

    @classmethod
    def zeros(cls, *args):
        arr = np.zeros(*args, dtype=np.int64)
        return arr.view(cls)

    @classmethod
    def arange(cls, *args):
        arr = np.arange(*args, dtype=np.int64) % MOD
        return arr.view(cls)

    @classmethod
    def ones(cls, *args):
        arr = np.ones(*args, dtype=np.int64)
        return arr.view(cls)

    @classmethod
    def _set_constant_array(cls, N):
        x = cls.arange(N)
        x[0] = 1
        fact = x.cumprod()   # cumprod maison
        x = cls.arange(N, 0, -1)
        x[0] = pow(int(fact[-1]), MOD-2, MOD)
        fact_inv = x.cumprod()[::-1]
        inv = cls.zeros(N)
        inv[1:N] = fact_inv[1:N] * fact[0:N-1]
        fact.flags.writeable = False  # beurk mais bon
        fact_inv.flags.writeable = False
        inv.flags.writeable = False
        cls._fact = fact
        cls._fact_inv = fact_inv
        cls._inverse = inv

    @classmethod
    def fact(cls, N):
        if not hasattr(cls, '_fact') or len(cls._fact) < N:
            cls._set_constant_array(max(N, 10 ** 6))
        return cls._fact[:N]

    @classmethod
    def fact_inv(cls, N):
        if not hasattr(cls, '_fact') or len(cls._fact) < N:
            cls._set_constant_array(max(N, 10 ** 6))
        return cls._fact_inv[:N]

    @classmethod
    def inverse(cls, N):
        if not hasattr(cls, '_fact') or len(cls._fact) < N:
            cls._set_constant_array(max(N, 10 ** 6))
        return cls._inverse[:N]

    def print(self, sep=' '):
        print(sep.join(map(str, self)))

    @classmethod
    def convolve_small(cls, f, g):
        lf, lg = len(f), len(g)
        l = lf + lg - 1
        if min(lf, lg) < 100 or (lf + lg) < 300:
            return (np.convolve(f, g) % MOD).view(cls)
        else:
            fft = np.fft.rfft
            ifft = np.fft.irfft
            n = 1 << l.bit_length()
            return (np.rint(ifft(fft(f, n) * fft(g, n))[:l]).astype(np.int64) % MOD).view(cls)

    @classmethod
    def convolve(cls, f, g, fft_killer=False):
        lf = len(f)
        lg = len(g)
        if lf < lg:
            f, g = g, f  # plus long d'abord, ça aide peut-être...
            lf, lg = lg, lf
        if lg <= (1 << 17) or (not fft_killer):
            fl = f & ((1 << 15) - 1)
            fh = f >> 15
            gl = g & ((1 << 15) - 1)
            gh = g >> 15
            x = cls.convolve_small(fl, gl)
            z = cls.convolve_small(fh, gh)
            y = cls.convolve_small(fl + fh, gl + gh) - x - z
            return x + (y << 15) + (z << 30)
        g = g.resize(lf)
        n = lf // 2
        fl = f[:n]
        fh = f[n:].copy()
        gl = g[:n]
        gh = g[n:].copy()
        x = ModArray.convolve(fl, gl)
        z = ModArray.convolve(fh, gh)
        fh[:len(fl)] += fl
        gh[:len(gl)] += gl
        y = ModArray.convolve(fh, gh)
        P = x.resize(lf + lf)
        P[n: n+len(x)] -= x
        P[n: n+len(y)] += y
        P[n: n+len(z)] -= z
        P[n+n: n+n+len(z)] += z
        return P[:lf + lg - 1]

    def resize(self, n):
        l = len(self)
        if l >= n:
            return self[:n]
        arr = np.resize(self, n).view(type(self))
        arr[l:] = 0
        return arr

    def diff(self):
        return np.diff(self) % MOD

    def cumprod(self):
        l = len(self)
        lsq = int(l ** 0.5 + 1)
        a = self.resize(lsq ** 2).reshape(lsq, lsq)
        for n in range(1, lsq):
            a[:, n] *= a[:, n-1]
        for n in range(1, lsq):
            a[n] *= a[n-1, -1]
        return a.ravel()[:l]

    def __array_wrap__(self, out_arr, context=None):
        if out_arr.dtype == np.int64:
            if context and context[0] == np.mod:
                return out_arr
            np.mod(out_arr, MOD, out=out_arr)
            return out_arr
        return np.asarray(out_arr)

# On continue...
P = ModArray(P)
fact = ModArray.fact(N+10)
fact_inv = ModArray.fact_inv(N+10)

# Q doit être la convolution qui fait tout le taf
Q = ModArray.convolve(P * fact[:N], fact_inv[:N][::-1])[N-1:]
Q *= fact_inv[:N]

# Petit calcul, sûrement du binomial mélangé à un chelou truc
x = fact[N] * fact_inv[:N+1] * fact_inv[:N+1][::-1] * N
x[:-1] -= Q

# Affichage ligne à ligne (je préfère print mais bon...)
x[1:].print(sep='\n')