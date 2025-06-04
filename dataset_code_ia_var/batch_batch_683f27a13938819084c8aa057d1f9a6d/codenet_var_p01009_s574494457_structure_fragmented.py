class WeightedUnionSet:
    def __init__(self, nmax):
        self._init_ws(nmax)
        self._init_par(nmax)
        self._init_power(nmax)
    def _init_ws(self, nmax):
        self.ws = [0] * nmax
    def _init_par(self, nmax):
        self.par = [-1] * nmax
    def _init_power(self, nmax):
        self.power = [0] * nmax
    def find(self, x):
        return self._find_helper(x)
    def _find_helper(self, x):
        if self._is_root(x):
            return x
        parent = self._find_helper(self.par[x])
        self._update_ws(x)
        self._update_par(x, parent)
        return parent
    def _is_root(self, x):
        return self.par[x] < 0
    def _update_ws(self, x):
        self.ws[x] += self.ws[self.par[x]]
    def _update_par(self, x, parent):
        self.par[x] = parent
    def weight(self, x):
        self._force_find(x)
        return self.ws[x]
    def _force_find(self, x):
        self.find(x)
    def connected(self, x, y):
        return self.find(x) == self.find(y)
    def unite(self, x, y, w):
        w = self._compute_w(x, y, w)
        x_root = self.find(x)
        y_root = self.find(y)
        if self._same_root(x_root, y_root):
            return 0
        x_root, y_root, w = self._root_order(x_root, y_root, w)
        self._unite_sets(x_root, y_root, w)
        return 1
    def _compute_w(self, x, y, w):
        w += self._power_get(x) + self.weight(x)
        w -= self._power_get(y) + self.weight(y)
        return w
    def _power_get(self, idx):
        return self.power[idx]
    def _same_root(self, x_root, y_root):
        return x_root == y_root
    def _root_order(self, x, y, w):
        if self.par[y] < self.par[x]:
            return y, x, -w
        return x, y, w
    def _unite_sets(self, x_root, y_root, w):
        self.par[x_root] += self.par[y_root]
        self.par[y_root] = x_root
        self.ws[y_root] = w
    def diff(self, x, y):
        if not self.connected(x, y):
            return [0, None]
        return [1, self._ws_diff(x, y)]
    def _ws_diff(self, x, y):
        return self.ws[x] - self.ws[y]

def read_input():
    return input().split()

def parse_nq(inputs):
    return int(inputs[0]), int(inputs[1])

def create_union_set(n):
    return WeightedUnionSet(n + 1)

def process_queries(Q, uf):
    for _ in range(Q):
        query = read_input()
        if is_in_query(query):
            process_in_query(query, uf)
        else:
            process_diff_query(query, uf)

def is_in_query(query):
    return query[0] == "IN"

def process_in_query(query, uf):
    a, b, c = extract_in_params(query)
    increment_power(uf, a, c)
    increment_power(uf, b, c)
    unite_sets_with_w(uf, a, b, c)

def extract_in_params(query):
    return int(query[1]), int(query[2]), int(query[3])

def increment_power(uf, idx, val):
    uf.power[idx] += val

def unite_sets_with_w(uf, a, b, c):
    uf.unite(a, b, c)

def process_diff_query(query, uf):
    a, b = extract_diff_params(query)
    if not uf.connected(a, b):
        handle_warning()
    else:
        print_diff_result(uf, a, b)

def extract_diff_params(query):
    return int(query[1]), int(query[2])

def handle_warning():
    print("WARNING")

def print_diff_result(uf, a, b):
    result = calculate_diff(uf, a, b)
    print(result)

def calculate_diff(uf, a, b):
    value_a = uf.power[a] + uf.ws[a]
    value_b = uf.power[b] + uf.ws[b]
    return value_b - value_a

def main():
    nq = read_input()
    N, Q = parse_nq(nq)
    uf = create_union_set(N)
    process_queries(Q, uf)

main()