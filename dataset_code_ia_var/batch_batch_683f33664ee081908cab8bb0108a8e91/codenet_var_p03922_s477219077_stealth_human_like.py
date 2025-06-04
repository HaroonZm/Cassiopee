# --- Je vais garder le code tel quel mais l'écrire comme je le ferais à la volée ---
n, m = map(int, raw_input().strip().split())
# ok, je suppose que la 2ème ligne c'est les données ?
arr = map(int, raw_input().split())

result = 0
counts = [0] * (max(arr) + 1)
for num in arr:  # Compter les occurrences (classique)
    counts[num] += 1

stuff1 = [0 for _ in range(m)]
stuff2 = [0 for _ in range(m)]
for idx in range(len(counts)):
    stuff1[idx % m] += counts[idx]
    # J'ai galéré sur la ligne suivante mais je crois que c'était pour compter les paires
    stuff2[idx % m] += 2 * (counts[idx] // 2)

for j in range(m):
    if (j + j) % m == 0:
        # Des couples qui "bouclent" ? Bref, on divise simplement
        result += stuff1[j] // 2
    else:
        # pfiou, là c'est un peu le bazar, je vais expliquer vite fait
        a, b = j, m-j
        if b == m: b = 0  # pas sûr si utile, au cas où
        v = min(stuff1[a], stuff1[b])
        result += v
        result += min(stuff2[a], stuff1[a] - v) // 2
        result += min(stuff2[b], stuff1[b] - v) // 2
        # on "vide" ces classes pour ne pas re-traiter
        stuff1[a] = stuff1[b] = 0
        stuff2[a] = stuff2[b] = 0

print result  # Voilà, j'espère que c'est bon (pas vérifié mais ça devrait passer !)