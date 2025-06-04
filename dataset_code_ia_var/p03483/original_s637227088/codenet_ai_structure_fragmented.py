class Bit:
    def __init__(self, n):
        self.size = n
        self.tree = self._make_tree(n)

    def _make_tree(self, n):
        return [0] * (n + 1)

    def __iter__(self):
        return self._bit_iterator()

    def _bit_iterator(self):
        return self._bit_iterator_gen()

    def _bit_iterator_gen(self):
        psum = self._init_psum()
        for i in self._get_range(self.size):
            csum = self.sum(i + 1)
            yield self._get_bit_value(csum, psum)
            psum = self._update_psum(csum)
        self._end_iterator()

    def _init_psum(self):
        return 0

    def _get_range(self, n):
        return range(n)

    def _get_bit_value(self, csum, psum):
        return csum - psum

    def _update_psum(self, csum):
        return csum

    def _end_iterator(self):
        raise StopIteration()

    def __str__(self):
        return self._str_bit()

    def _str_bit(self):
        return str(self._to_list())

    def _to_list(self):
        return list(self)

    def sum(self, i):
        self._check_sum_index(i)
        s = self._sum_init()
        while self._sum_cond(i):
            s = self._sum_add(s, self._sum_tree_val(i))
            i = self._sum_update_i(i)
        return s

    def _check_sum_index(self, i):
        if not (0 <= i <= self.size):
            self._raise_value_error()

    def _raise_value_error(self):
        raise ValueError("error!")

    def _sum_init(self):
        return 0

    def _sum_cond(self, i):
        return i > 0

    def _sum_add(self, s, v):
        return s + v

    def _sum_tree_val(self, i):
        return self.tree[i]

    def _sum_update_i(self, i):
        return i - (i & -i)

    def add(self, i, x):
        self._check_add_index(i)
        i = self._increment_index(i)
        while self._add_cond(i):
            self._add_update_tree(i, x)
            i = self._add_update_i(i)

    def _check_add_index(self, i):
        if not (0 <= i < self.size):
            self._raise_value_error()

    def _increment_index(self, i):
        return i + 1

    def _add_cond(self, i):
        return i <= self.size

    def _add_update_tree(self, i, x):
        self.tree[i] += x

    def _add_update_i(self, i):
        return i + (i & -i)

    def __getitem__(self, key):
        self._check_item_index(key)
        return self._get_bititem(key)

    def _check_item_index(self, key):
        if not (0 <= key < self.size):
            self._raise_index_error()

    def _raise_index_error(self):
        raise IndexError("error!")

    def _get_bititem(self, key):
        return self.sum(key + 1) - self.sum(key)

    def __setitem__(self, key, value):
        self._check_item_index(key)
        self._set_bititem(key, value)

    def _set_bititem(self, key, value):
        self.add(key, value - self[key])

def main():
    S = get_input()
    N = get_length(S)
    cnt = make_count_array()
    count_characters(S, cnt)
    odd = check_odd_count(cnt)
    halve_counts(cnt)
    L = make_L()
    n = get_initial_n(N)
    B = build_B(S, cnt, L, n, odd)
    bit = create_bit(N)
    ans = compute_answer(B, bit)
    output(ans)

def get_input():
    return input()

def get_length(S):
    return len(S)

def make_count_array():
    return [0]*26

def count_characters(S, cnt):
    for c in S:
        update_count(cnt, c)

def update_count(cnt, c):
    cnt[ord(c)-97] += 1

def check_odd_count(cnt):
    odd = -1
    for i, cn in enumerate(cnt):
        if is_odd(cn):
            if odd == -1:
                odd = i
            else:
                handle_multiple_odds()
    return odd

def is_odd(n):
    return n % 2 != 0

def handle_multiple_odds():
    print(-1)
    exit()

def halve_counts(cnt):
    for i in range(len(cnt)):
        halve_count_at(cnt, i)

def halve_count_at(cnt, i):
    cnt[i] //= 2

def make_L():
    return [[] for _ in range(26)]

def get_initial_n(N):
    return (N // 2) + 1

def build_B(S, cnt, L, n, odd):
    B = []
    L_local = [l.copy() for l in L]
    cnt_local = cnt.copy()
    state = {
        'B': B,
        'cnt': cnt_local,
        'L': L_local,
        'n': n,
        'odd': odd,
    }
    for c in S:
        build_B_for_char(state, c)
    return state['B']

def build_B_for_char(state, c):
    c_int = char_to_int(c)
    if state['cnt'][c_int] == 0:
        handle_zero_count(state, c_int)
    else:
        handle_nonzero_count(state, c_int)

def char_to_int(c):
    return ord(c) - 97

def handle_zero_count(state, c_int):
    if is_odd_char(state, c_int):
        append_odd(state)
        mark_odd_processed(state)
    else:
        p = pop_L(state, c_int)
        append_B(state, p)

def is_odd_char(state, c_int):
    return c_int == state['odd']

def append_odd(state):
    state['B'].append(1)

def mark_odd_processed(state):
    state['odd'] = -1

def pop_L(state, c_int):
    return state['L'][c_int].pop()

def append_B(state, value):
    state['B'].append(value)

def handle_nonzero_count(state, c_int):
    append_L(state, c_int)
    append_zero_B(state)
    decrement_n(state)
    decrement_cnt(state, c_int)

def append_L(state, c_int):
    state['L'][c_int].append(state['n'])

def append_zero_B(state):
    state['B'].append(0)

def decrement_n(state):
    state['n'] -= 1

def decrement_cnt(state, c_int):
    state['cnt'][c_int] -= 1

def create_bit(N):
    return Bit(N//2+2)

def compute_answer(B, bit):
    ans = 0
    for i, b in enumerate(B):
        ans = update_answer(ans, i, b, bit)
        update_bit(bit, b)
    return ans

def update_answer(ans, i, b, bit):
    return ans + i - bit.sum(b+1)

def update_bit(bit, b):
    bit.add(b, 1)

def output(ans):
    print(ans)

main()