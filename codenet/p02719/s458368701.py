n, k = map(int, input().split())

n_k_amari = n % k
n_k_1 = k - n_k_amari

print(min(n, n_k_amari, n_k_1))