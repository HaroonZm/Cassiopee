import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], ), cache=True)
def copy_array(arr):
    return arr.copy()

@njit((i8[:], ), cache=True)
def build_bit(raw_data):
    bit = copy_array(raw_data)
    for i in range(len(bit)):
        update_bit_on_build(bit, i)
    return bit

@njit((i8[:], i8), cache=True)
def get_sum(bit, i):
    s = 0
    while i:
        s = accumulate_sum(bit, i, s)
        i = decrement_index(i)
    return s

@njit((i8[:], i8), cache=True)
def accumulate_sum(bit, i, s):
    return s + bit[i]

@njit((i8[:], i8, i8), cache=True)
def add(bit, i, x):
    while index_in_range(i, len(bit)):
        bit[i] = add_to_bit(bit[i], x)
        i = increment_index(i)
        
@njit(inline='always')
def update_bit_on_build(bit, i):
    j = i + (i & (-i))
    if j < len(bit):
        bit[j] += bit[i]

@njit(inline='always')
def decrement_index(i):
    return i - (i & -i)

@njit(inline='always')
def increment_index(i):
    return i + (i & -i)

@njit(inline='always')
def add_to_bit(val, x):
    return val + x

@njit(inline='always')
def index_in_range(i, n):
    return i < n

@njit((i8[:], i8), cache=True)
def find_kth_element(bit, k):
    N = len(bit)
    x, sx = 0, 0
    dx = calc_initial_dx(N)
    while dx:
        x, sx = advance_kth(bit, N, x, sx, dx, k)
        dx = halve(dx)
    return x + 1

@njit(inline='always')
def calc_initial_dx(N):
    dx = 1
    while 2 * dx < N:
        dx *= 2
    return dx

@njit(inline='always')
def halve(dx):
    return dx // 2

@njit(inline='always')
def advance_kth(bit, N, x, sx, dx, k):
    y = x + dx
    if y < N:
        sy = sx + bit[y]
        if sy < k:
            x, sx = y, sy
    return x, sx

@njit((i8, i8[:]), cache=True)
def main(N, AB):
    A, B = split_AB(AB)
    Q = len(A)
    bit, bit_raw, H = init_structs(N)
    set_H0(H)
    setup_bit(bit_raw, bit, N)
    for i in range(Q):
        do_query(A, B, i, bit, bit_raw, H)
    propagate_H(N, H)
    return H[1:N + 1]

@njit(inline='always')
def split_AB(AB):
    return AB[::2], AB[1::2]

@njit(inline='always')
def init_structs(N):
    bit = np.zeros(N + 1, np.int64)
    bit_raw = np.zeros(N + 1, np.int64)
    H = np.zeros(N + 1, np.int64)
    return bit, bit_raw, H

@njit(inline='always')
def set_H0(H):
    H[0] = 2 * 10**13 + 10

@njit(inline='always')
def setup_bit(bit_raw, bit, N):
    bit_raw[N] = 1
    add(bit, N, 1)

@njit((i8[:], i8[:], i8, i8[:], i8[:], i8[:]), cache=True)
def do_query_by_args(A, B, i, bit, bit_raw, H):
    do_query(A, B, i, bit, bit_raw, H)

@njit(inline='always')
def do_query(A, B, i, bit, bit_raw, H):
    a, b = A[i], B[i]
    n = get_sum(bit, a - 1)
    h = H[find_kth_element(bit, 1 + n)]
    if not bit_raw[a]:
        process_new_a(bit_raw, bit, a, h, H)
    r = a
    process_b(bit, bit_raw, H, r, n, b)

@njit(inline='always')
def process_new_a(bit_raw, bit, a, h, H):
    bit_raw[a] = 1
    add(bit, a, 1)
    H[a] = h

@njit(inline='always')
def process_b(bit, bit_raw, H, r, n, b):
    while b:
        l = choose_l(bit, n)
        n -= 1
        area = compute_area(H, l, r)
        if area <= b:
            b = remove_area(b, area)
            if l:
                remove_l(bit_raw, bit, l)
            copy_height(H, l, r)
            continue
        k = area_division(b, r, l)
        b = subtract_k_area(b, k, r, l)
        H[r] = add_height(H[r], k)
        if b:
            m = l + b
            set_new_partition(bit_raw, bit, m, H, H[r])
            b = 0

@njit(inline='always')
def choose_l(bit, n):
    return 0 if n == 0 else find_kth_element(bit, n)

@njit(inline='always')
def compute_area(H, l, r):
    return (H[l] - H[r]) * (r - l)

@njit(inline='always')
def remove_area(b, area):
    return b - area

@njit(inline='always')
def remove_l(bit_raw, bit, l):
    bit_raw[l] = 0
    add(bit, l, -1)

@njit(inline='always')
def copy_height(H, l, r):
    H[l], H[r] = 0, H[l]

@njit(inline='always')
def area_division(b, r, l):
    return b // (r - l)

@njit(inline='always')
def subtract_k_area(b, k, r, l):
    return b - k * (r - l)

@njit(inline='always')
def add_height(h, k):
    return h + k

@njit(inline='always')
def set_new_partition(bit_raw, bit, m, H, h):
    bit_raw[m] = 1
    add(bit, m, 1)
    H[m] = h + 1

@njit(inline='always')
def propagate_H(N, H):
    for n in range(N, 0, -1):
        H[n - 1] = max(H[n - 1], H[n])

def read_input():
    N, Q = map(int, readline().split())
    AB = np.array(read().split(), np.int64)
    return N, AB

def output_result(ans):
    print('\n'.join(map(str, ans.tolist())))

def main_wrapper():
    N, AB = read_input()
    ans = main(N, AB)
    output_result(ans)

if __name__ == "__main__":
    main_wrapper()