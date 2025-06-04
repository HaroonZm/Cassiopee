# Lire deux entiers à partir de l'entrée standard, séparés par un espace.
# Le premier entier 'n' représente le nombre d'intervalles à traiter.
# Le second entier 't' est lu mais n'est pas utilisé dans la suite du code.
n, t = map(int, input().split())

# Initialiser une liste vide nommée 'box'.
# Cette liste contiendra des tuples représentant les points d'entrée et de sortie des intervalles.
box = []

# Boucle qui va se répéter 'n' fois (une fois pour chaque intervalle).
for _ in range(n):
    # Lire deux entiers supplémentaires à chaque itération (les bornes de l'intervalle).
    # 's' est la borne de début de l'intervalle, 't' celle de fin.
    s, t = map(int, input().split())
    
    # Ajouter un tuple (s, 1) dans la liste 'box'.
    # Ce tuple signifie qu'il y a une entrée dans un intervalle au point 's'.
    box.append((s,1))
    
    # Ajouter un tuple (t, 0) dans la liste 'box'.
    # Ce tuple signifie qu'il y a une sortie d'intervalle au point 't'.
    box.append((t,0))

# Trier la liste 'box' selon les valeurs du premier élément du tuple (c'est-à-dire ordinalement selon les points sur l'axe).
# Cela regroupe tous les débuts et toutes les fins d'intervalles en ordre croissant.
box = sorted(box)

# Initialiser une variable 'cnt' à 0.
# 'cnt' représentera le nombre courant d'intervalles actifs à chaque point.
cnt = 0

# Initialiser une variable 'ans' à 0.
# 'ans' gardera la trace du plus grand nombre d'intervalles actifs rencontrés jusqu'à présent.
ans = 0

# Parcourir chaque tuple (x) de la liste triée 'box'.
for x in box:
    # Extraire les valeurs 'a' et 'b' du tuple 'x'.
    # 'a' est le point actuel (de début ou de fin d'intervalle).
    # 'b' indique le type : '1' pour un début d'intervalle, '0' pour une fin.
    a, b = x
    
    # Si 'b' vaut 0, cela signifie que l'on est à une fin d'intervalle.
    # On décrémente alors le compteur 'cnt' car un intervalle se termine.
    if b == 0:
        cnt -= 1
    # Si 'b' vaut 1, cela signifie que l'on est à un début d'intervalle.
    # On incrémente alors le compteur 'cnt' car un nouvel intervalle commence.
    else:
        cnt += 1
    
    # Calculer le maximum actuel entre 'ans' et 'cnt' et mettre à jour 'ans' si 'cnt' est plus élevé.
    # Cela permet de conserver le nombre maximal d'intervalles actifs observé jusqu'à présent.
    ans = max(ans,cnt)

# Afficher la valeur finale de 'ans', qui est le maximum d'intervalles actifs relevé simultanément.
print(ans)