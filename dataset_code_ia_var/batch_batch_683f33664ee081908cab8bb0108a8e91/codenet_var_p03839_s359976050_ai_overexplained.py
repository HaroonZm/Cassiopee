# Lire une ligne d'entrée, la séparer par les espaces, convertir chaque élément en entier, puis assigner respectivement les valeurs à n et k.
n, k = map(int, input().split())

# Lire une ligne d'entrée, la séparer par espaces, convertir chaque élément en entier, et former la liste des valeurs 'a'.
a = list(map(int, input().split()))

# Initialiser une liste 'asum' de taille n+1 remplie de zéros.
# 'asum' servira à stocker les sommes cumulées des éléments de 'a'. Chaque case i contiendra la somme des éléments a[0] à a[i-1].
asum = [0 for _ in range(n+1)]

# Initialiser une liste 'psum' de taille n+1 remplie de zéros.
# 'psum' servira à stocker les sommes cumulées partielles où seules les valeurs positives de 'a' sont retenues.
psum = [0 for _ in range(n+1)]

# Parcourir tous les indices de 0 à n-1 (inclus) pour construire les sommes cumulées.
for i in range(n):
    # A chaque itération, 'asum[i+1]' devient égal à 'asum[i]' (somme des valeurs précédentes) plus 'a[i]'.
    asum[i+1] = asum[i] + a[i]
    # À chaque itération, 'psum[i+1]' devient égal à 'psum[i]' (somme positive précédente) plus 'a[i]' si 'a[i]' est positif, sinon 0.
    psum[i+1] = psum[i] + max(0, a[i])

# Initialiser la variable de résultat 'ans' à 0. Cette variable stockera la meilleure réponse trouvée.
ans = 0

# Parcourir toutes les positions de départ possibles 'i' pour une sous-séquence de longueur k (de 0 à n-k inclus).
for i in range(n-k+1):
    # Calculer la somme maximum possible pour une fenêtre commençant à l'indice 'i' et de taille 'k'.
    # - psum[i] - psum[0] : somme des éléments positifs avant la fenêtre
    # - asum[i+k] - asum[i] : somme totale dans la fenêtre, que l'on prend telle quelle
    # - psum[n] - psum[i+k] : somme des éléments positifs après la fenêtre
    current = psum[i] - psum[0] + asum[i+k] - asum[i] + psum[n] - psum[i+k]

    # Met à jour 'ans' avec la valeur maximale entre 'ans' et 'current'
    ans = max(ans, current)

    # Calculer le cas où on ignore les éléments négatifs dans la fenêtre (aucun bonus associé à la fenêtre)
    # Il s'agit donc de la somme des positifs en dehors de la fenêtre
    current_wo_window = psum[i] - psum[0] + psum[n] - psum[i+k]

    # Met à jour 'ans' si ce cas donne une plus grande valeur
    ans = max(ans, current_wo_window)

# Afficher la réponse finale, qui correspond à la somme maximale atteignable selon les règles précédentes.
print(ans)