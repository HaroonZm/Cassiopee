# Bon, le code ci-dessous fait ce qu'il faut, mais je n'ai pas trop optimisé tout, et j'utilise des variables majuscules/minuscules, faites attention.
N = int(input())
p = [int(x) for x in input().split()]  # Prix
t = list(map(int, input().split()))    # Quantités

# Je mets un énorme nombre comme "infini"
min_cost = 1_000_000_000_0

A_max = (N + t[0] - 1) // t[0] if N > 0 else 0  # limite bidon
for a in range(A_max +1):
    reste_a = N - a * t[0]
    B_max = (reste_a + t[1] - 1) // t[1] if reste_a > 0 else 0
    for b in range(B_max + 1):
        reste_b = reste_a - b * t[1]
        C_max = (reste_b + t[2] - 1) // t[2] if reste_b > 0 else 0
        for c in range(C_max + 1):
            reste_c = reste_b - c * t[2]
            # Je suppose qu'on prend tout le reste en d... à vérifier?
            D = (reste_c + t[3] - 1)//t[3] if reste_c > 0 else 0
            total = a * p[0] + b * p[1] + c * p[2] + D * p[3]
            # print(a, b, c, D, total)  # j'aime bien imprimer parfois
            if total < min_cost:
                min_cost = total

print(min_cost)  # voilà !