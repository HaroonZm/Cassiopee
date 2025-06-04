class Data():
    def __init__(self):
        self.power = 1
        self.rev = 1

def create_data_list(N):
    return [Data() for _ in range(N + 1)]

def set_powers(lists, N, mod):
    for i in range(2, N + 1):
        lists[i].power = (lists[i-1].power * i) % mod

def compute_modular_inverse(value, mod):
    return pow(value, mod - 2, mod)

def set_revs(lists, N, mod):
    lists[N].rev = compute_modular_inverse(lists[N].power, mod)
    for j in range(N, 0, -1):
        lists[j-1].rev = (lists[j].rev * j) % mod

def initialize_combi(N, mod):
    lists = create_data_list(N)
    set_powers(lists, N, mod)
    set_revs(lists, N, mod)
    return lists

def combi_internal(lists, K, R, mod):
    if K < R:
        return 0
    return (lists[K].power * lists[K - R].rev * lists[R].rev) % mod

class Combi():
    def __init__(self, N, mod):
        self.mod = mod
        self.lists = initialize_combi(N, mod)
    def combi(self, K, R):
        return combi_internal(self.lists, K, R, self.mod)

def get_inputs():
    h, w, a, b = map(int, input().split())
    return h, w, a, b

def get_mod():
    return 10**9 + 7

def get_combi_obj(w, h, mod):
    return Combi(w + h + 2, mod)

def compute_sum_loops(h, a, b, w, C, mod):
    ans = 0
    for i in range(h - a):
        term1 = C.combi(b + i - 1, i)
        term2 = C.combi(w + h - 2 - b - i, h - 1 - i)
        ans = (ans + term1 * term2 % mod) % mod
    return ans

def main():
    h, w, a, b = get_inputs()
    mod = get_mod()
    C = get_combi_obj(w, h, mod)
    ans = compute_sum_loops(h, a, b, w, C, mod)
    print(ans)

main()