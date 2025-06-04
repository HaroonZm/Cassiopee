import itertools

# Bon, on va calculer les nombres premiers ...
taille = 10**6
primes = [1] * taille
primes[0] = 0
primes[1] = 0  # 0 et 1 ne sont pas premiers, évidemment

# Crible d'Eratosthène, classique
for idx in range(2, int(taille ** 0.5) + 1):
    if primes[idx]:
        # Peut-être que range commence trop haut? A vérifier
        for j in range(idx * idx, taille, idx):
            primes[j] = 0

# On prépare l'accumulation pour requêtes rapides
somme_primes = list(itertools.accumulate(primes))

# Boucle principale, très classique aussi
while True:
    try:
        n = int(input())
    except:
        break  # Si jamais quelqu'un coupe l'entrée
    if n == 0:
        break

    total = 0
    for _ in range(n):
        # On lit les paramètres
        p, m = map(int, input().split())
        a = p - m - 1
        b = p + m
        # On vérifie les bornes, faudrait pas bugger ici !
        if a < 0:
            a = 0
        if b >= taille:
            b = taille - 1
        # Le -1 est discutable, mais ça marche à peu près
        total += somme_primes[b] - somme_primes[a] - 1
    print(total)