# Programme pour compter le nombre de nombres premiers ≤ n pour plusieurs jeux de données
# Approche :
# 1. La valeur maximale possible de n est 999,999.
# 2. On va utiliser le crible d'Ératosthène pour pré-calculer tous les nombres premiers jusqu'à 999,999.
# 3. On construira un tableau cumulatif "prefix" où prefix[i] contient le nombre de premiers ≤ i.
# 4. Pour chaque entrée n, on affiche simplement prefix[n].
# Cette méthode est efficace pour gérer jusqu'à 30 requêtes.

import sys

MAX_N = 999999

# Crible d'Ératosthène pour identifier les nombres premiers jusqu'à MAX_N
is_prime = [True] * (MAX_N + 1)
is_prime[0] = False  # 0 n'est pas premier
is_prime[1] = False  # 1 n'est pas premier

for i in range(2, int(MAX_N ** 0.5) + 1):
    if is_prime[i]:
        for j in range(i * i, MAX_N + 1, i):
            is_prime[j] = False

# Pré-calcul du tableau cumulatif du nombre de premiers ≤ i
prefix = [0] * (MAX_N + 1)
count = 0
for i in range(1, MAX_N + 1):
    if is_prime[i]:
        count += 1
    prefix[i] = count

def main():
    # Lecture de plusieurs lignes jusqu'à la fin de l'entrée standard
    for line in sys.stdin:
        line = line.strip()
        if not line:
            continue
        n = int(line)
        # Afficher le nombre de nombres premiers ≤ n pré-calculé dans prefix
        print(prefix[n])

if __name__ == "__main__":
    main()