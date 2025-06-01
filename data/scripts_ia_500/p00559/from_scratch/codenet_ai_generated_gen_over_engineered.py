class AltitudeTrack:
    def __init__(self, initial_altitudes):
        self._altitudes = initial_altitudes
        self._n = len(initial_altitudes) - 1
    def get(self, idx):
        return self._altitudes[idx]
    def increase_range(self, left, right, x):
        # Efficient update will be done externally (here just to signify interface)
        for i in range(left, right + 1):
            self._altitudes[i] += x
    def current_diff(self):
        # returns differences A[i+1]-A[i] for i in 0..N-1
        return [self._altitudes[i+1] - self._altitudes[i] for i in range(self._n)]

class TemperatureModel:
    def __init__(self, S, T):
        self._S = S
        self._T = T
    def temperature_change(self, delta_altitude):
        if delta_altitude > 0:
            return -self._S * delta_altitude
        else:
            return self._T * (-delta_altitude)

class FenwickTree:
    def __init__(self, n):
        self._n = n
        self._tree = [0]*(n+1)
    def add(self, i, x):
        while i <= self._n:
            self._tree[i] += x
            i += i & -i
    def sum(self, i):
        s = 0
        while i > 0:
            s += self._tree[i]
            i -= i & -i
        return s
    def range_add(self, l, r, x):
        self.add(l, x)
        if r+1 <= self._n:
            self.add(r+1, -x)

class FoehnPhenomenaSolver:
    def __init__(self, N, Q, S, T, altitudes_initial):
        self._N = N
        self._Q = Q
        self._temp_model = TemperatureModel(S, T)
        # We'll maintain difference array D[i] = A[i+1] - A[i]
        self._diff = [altitudes_initial[i+1] - altitudes_initial[i] for i in range(N)]
        # Fenwick tree to record increments to the diff array
        self._fenw = FenwickTree(N)
        self._S = S
        self._T = T
        # Precompute initial temperature
        self._temp = 0
        for d in self._diff:
            self._temp += self._temp_model.temperature_change(d)
    def _get_diff(self, i):
        # i is 0-based index for diff array
        # diff[i] + fenw sum at i+1
        return self._diff[i] + self._fenw.sum(i+1)
    def _change_edge_temp(self, i, old_val, new_val):
        old_temp = self._temp_model.temperature_change(old_val)
        new_temp = self._temp_model.temperature_change(new_val)
        self._temp += (new_temp - old_temp)
    def process_move(self, L, R, X):
        # The impact of increasing a range in A (from L to R) by X on difference array:
        # difference array D changes:
        # D[L-1] += X if L > 1 (since A[L] - A[L-1] is affected)
        # D[R]   -= X if R < N  (since A[R+1] - A[R] is affected)
        # Update temp accordingly for these up to two edges

        # Adjust left edge if L > 1
        if L > 1:
            idx = L - 2  # zero-based index for diff
            old_val = self._get_diff(idx)
            new_val = old_val + X
            self._change_edge_temp(idx, old_val, new_val)
            self._fenw.range_add(idx+1, idx+1, X)  # fenw: 1-based
        # Adjust right edge if R < N
        if R < self._N:
            idx = R - 1  # zero-based index for diff
            old_val = self._get_diff(idx)
            new_val = old_val - X
            self._change_edge_temp(idx, old_val, new_val)
            self._fenw.range_add(idx+1, idx+1, -X)

        # The altitudes are logically updated by this operation but stored only implicitly
        # Temperature is updated incrementally

        return self._temp

def main():
    import sys
    sys.setrecursionlimit(10**7)
    input = sys.stdin.readline

    N,Q,S,T = map(int,input().split())
    altitudes_initial = [int(input()) for _ in range(N+1)]
    solver = FoehnPhenomenaSolver(N,Q,S,T, altitudes_initial)
    for _ in range(Q):
        L,R,X = map(int,input().split())
        res = solver.process_move(L,R,X)
        print(res)

if __name__ == "__main__":
    main()