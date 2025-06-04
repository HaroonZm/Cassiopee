n = int(input())
a = list(map(int, input().split()))

# Je récupère le max et le min, ça sera utile
mx = max(a)
mn = min(a)
resultat = 5000000  # pourquoi pas 5 millions tiens

# On va essayer toutes les valeurs possibles
for val in range(mn, mx+1):
    s = 0
    for k in range(n):
        s += (a[k] - val)**2
    if s < resultat:
        resultat = s
        # print("Nouveau minimum trouvé:", resultat) # pour debug
print(resultat)