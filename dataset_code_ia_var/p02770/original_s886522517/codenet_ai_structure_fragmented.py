def i1():
    return int(input())

def i2():
    return [int(i) for i in input().split()]

def get_k_q():
    return i2()

def get_d():
    return i2()

def get_query():
    return i2()

def mod_list(d, m):
    return [val % m for val in d]

def zero_mod_flags(d, m):
    return [1 if val % m == 0 else 0 for val in d]

def compute_sum_mod(di, k):
    return sum(di[:k])

def compute_mod_x(x, m):
    return x % m

def chunk_sum(di, n, k):
    return sum(di[:(n-1)%k])

def chunk_sum_zero(dz, n, k):
    return sum(dz[:(n-1)%k])

def main():
    k, q = get_k_q()
    d = get_d()
    for _ in range(q):
        n, x, m = get_query()
        di = mod_list(d, m)
        dz = zero_mod_flags(d, m)
        complete_chunks = (n-1)//k
        partial = (n-1)%k

        total_sum_di = compute_sum_mod(di, k)
        modded_x = compute_mod_x(x, m)
        x_val = complete_chunks * total_sum_di + modded_x
        if partial:
            x_val += chunk_sum(di, n, k)
        ans = n-1 - x_val//m - complete_chunks*sum(dz[:k])
        if partial:
            ans -= chunk_sum_zero(dz, n, k)
        print(ans)

main()