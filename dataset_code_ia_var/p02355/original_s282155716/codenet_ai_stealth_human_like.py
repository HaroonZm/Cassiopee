import sys

# Lecture des données, un classique...
n, k = map(int, input().split())
a = list(map(int, input().split()))
# On va essayer d'être safe
mx = max(max(a), n, k) + 3
chk = [0] * mx

# On compte combien chaque valeur apparait, sauf que là on est pas sûr si ça sert vraiment plus tard
for v in a:
    chk[v] += 1

# Si jamais il manque un nombre de 1 à k, clairement on peut abandonner
for i in range(1, k+1):
    if chk[i] == 0:
        print(0)
        sys.exit()  # trop la flemme de continuer si c'est déjà foutu

# Bon, reset le compteur pour la suite
for v in a:
    chk[v] = 0

left = 0
right = 0
diff = 0
res = n + 1  # On met un max bien large
while right < n:
    # On ajoute a[right] à notre fenêtre
    chk[a[right]] += 1
    if chk[a[right]] == 1 and 1 <= a[right] <= k:
        diff += 1

    while diff == k:
        # Fenêtre valide
        res = min(res, right - left + 1)
        chk[a[left]] -= 1
        if chk[a[left]] == 0 and 1 <= a[left] <= k:
            diff -= 1
        left += 1
    right += 1

# Un peu oldschool mais ça fait le job
print(res if res <= n else 0)