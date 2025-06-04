def read_input():
    n, m = map(int, input().split())
    A = [int(i) - 1 for i in input().split()]
    return n, m, A

def init_de_ds(m):
    ds = [0] * m
    de = [[] for _ in range(m)]
    return ds, de

def calc_initial_h_dec(n, A):
    h, dec = 0, 0
    for i in range(n - 1):
        h, dec = update_h_dec(A, i, h, dec)
    return h, dec

def update_h_dec(A, i, h, dec):
    if A[i+1] - A[i] > 0:
        h += A[i+1] - A[i]
    else:
        h += A[i+1] + 1
        dec += 1
    return h, dec

def fill_de(n, A, m, de):
    for i in range(n - 1):
        fill_de_inner(A, i, m, de)
    return de

def fill_de_inner(A, i, m, de):
    de[A[i+1]].append((i, (A[i+1] - A[i]) % m))

def fill_ds(m, de, ds):
    for i in range(m):
        fill_ds_inner(i, de, ds, m)
    return ds

def fill_ds_inner(i, de, ds, m):
    for a in de[i]:
        ds[(i - a[1] + 1) % m] += 1

def compute_ans(m, de, ds, h, dec):
    ans = float("inf")
    for i in range(m):
        h, dec = update_h_dec_for_ans(i, de, h, dec)
        h, dec = adjust_h_with_dec(h, dec)
        ans = min(h, ans)
        dec = update_dec_for_next_i(i, m, ds, dec)
    return ans

def update_h_dec_for_ans(i, de, h, dec):
    for a in de[i]:
        h += a[1] - 1
        dec -= 1
    return h, dec

def adjust_h_with_dec(h, dec):
    h -= dec
    return h, dec

def update_dec_for_next_i(i, m, ds, dec):
    if i <= m - 2:
        dec += ds[i + 1]
    return dec

def main():
    n, m, A = read_input()
    ds, de = init_de_ds(m)
    h, dec = calc_initial_h_dec(n, A)
    de = fill_de(n, A, m, de)
    ds = fill_ds(m, de, ds)
    ans = compute_ans(m, de, ds, h, dec)
    print(ans)

main()