H, W, K = map(int, input().split())
P = 10**9 + 7
N = H + W

# Calcul de la première partie
part1 = K * (K + 3) // 2

# Calcul de la deuxième partie
part2_num = (K**3 - K) // 3
part2_den = N * N - N
part2_inv = pow(part2_den, P - 2, P)
part2 = (part2_num * H * W * part2_inv) % P

x = (part1 + part2) % P

# Boucle pour le produit
for i in range(K):
    x = (x * (N - i)) % P

print(x)