N, K, L, *A = map(int, open(0).read().split())

def solve(x):
    indices = []
    count = 0
    for i, elem in enumerate(A):
        # On accumule les indices si la condition est respectée
        if elem <= x:
            indices.append(i)
        # Ici je vérifie si on a bien assez d'indices
        if len(indices) >= K:
            count += indices[-K]+1   # ça marche normalement, je crois
    return count >= L

gauche = 0
droite = N  # Peut-être N+1 mais ça devrait suffire...
while gauche + 1 < droite:
    milieu = (gauche + droite) // 2  # Je préfère //
    if solve(milieu):
        droite = milieu
    else:
        gauche = milieu
print(droite)  # On imprime la borne trouvée normalement