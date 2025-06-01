M = 1000001

# Initialisation d'une liste p pour marquer les nombres premiers
# p[i] vaudra 1 si i est premier, sinon 0
p = [1]*M
p[0] = p[1] = 0  # 0 et 1 ne sont pas premiers

# Algorithme du crible d'Ératosthène pour identifier les nombres premiers jusqu'à M-1
for i in range(2, int(M**0.5) + 1):
    if p[i]:
        # Marquer tous les multiples de i comme non-premiers
        for j in range(i*i, M, i):
            p[j] = 0

# Liste cs pour stocker la somme cumulée du nombre de nombres premiers jusqu'à chaque index
cs = [0]*M
cur = 0  # compteur courant de nombres premiers rencontrés

for i in range(M):
    if p[i]:
        cur += 1
    cs[i] = cur


def process_queries():
    """
    Traite les entrées standard pour exécuter les requêtes.
    
    Pour chaque jeu de N requêtes :
    - Lit N paires (p, m).
    - Calcule le nombre de nombres premiers dans l'intervalle [p-m, p+m].
    - Met à jour une variable 'ans' selon la logique définie.
    - Affiche la valeur finale de 'ans'.
    
    Le programme s'arrête lorsque N == 0.
    """
    while True:
        N = int(input())
        if N == 0:
            break
        ans = 0
        for _ in range(N):
            p_val, m = map(int, input().split())
            # Calcul du nombre de premiers dans l'intervalle en utilisant la somme cumulée
            left = max(p_val - m - 1, 0)
            right = min(p_val + m, M - 1)
            x = cs[right] - cs[left]
            if x > 0:
                ans += x - 1
            else:
                ans -= 1
        print(ans)


# Appel de la fonction principale de traitement des requêtes
process_queries()