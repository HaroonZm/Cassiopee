# Prend une entrée utilisateur et la convertit en entier ; cela représente le nombre de lignes suivantes qui décrivent les sons de base possibles.
N = int(input())

# Initialise un dictionnaire vide appelé 'ph'; il servira à mapper chaque valeur d'intervalle à son poids de base optimal (p).
ph = {}
# Boucle sur chaque ligne décrivant un ensemble d'intervalles, leurs poids.
for i in range(N):
    # Prend une ligne d'entrée utilisateur et sépare les trois valeurs ; chacune est convertie en entier. 
    # Ici, s = début d'intervalle, l = fin d'intervalle, p = poids associé.
    s,l,p = map(int,input().split())
    # Pour chaque nombre entier 'j' de s à l inclusivement.
    for j in range(s,l+1):
        # Si 'j' n'est pas déjà une clé dans le dictionnaire 'ph', on l'ajoute avec la valeur 'p'.
        if j not in ph:
            ph[j] = p
        # Sinon, la clé existe déjà, on conserve dans ph[j] le maximum entre la valeur déjà présente et 'p'.
        else:
            ph[j] = max(p, ph[j])

# Prend une autre entrée utilisateur, le nombre d'éléments de la mélodie à traiter.
M = int(input())
# Initialise une liste vide qui contiendra les valeurs correspondant à la mélodie à rechercher dans la phrase.
melody = []
# Boucle autant de fois que de notes/mélodies à lire.
for i in range(M):
    # Ajoute à la liste 'melody' une valeur entière lue à l'entrée standard. Elle correspond à une valeur de note/longueur à récupérer.
    melody.append(int(input()))

# #print(ph)  # Ligne commentée : aurait affiché le dictionnaire des intervalles et poids maximaux.

# Crée une liste 'phrase' de taille 394 (indices 0 à 393 inclus), initialisée avec des zéros.
# L'indice de la liste correspondra à une longueur spécifique de phrase ; la valeur mémorisera le score maximal réalisable.
phrase = [0 for i in range(393+1)]

# Pour chaque intervalle 'k' (clé) et son poids maximal 'p' dans le dictionnaire ph...
for k,p in ph.items():
    # On tente d'utiliser ce poids (p, lié à l'intervalle k) pour bonifier tous les scores des phrases de longueur j >= k.
    for j in range(k,393+1):
        # Si la somme du score pour une phrase de longueur (j-k) plus 'p' est supérieure au meilleur score qu'on a déjà pour la longueur 'j',
        # on le remplace par cette nouvelle valeur maximale.
        if phrase[j] < phrase[j-k] + p:
            phrase[j] = phrase[j-k] + p

# On crée une liste 'ans' qui contient le score maximal pour chaque longueur demandée dans melody, mais seulement si ce score est non nul.
ans = [phrase[i] for i in melody if phrase[i]]

# Si la longueur de la liste 'ans' correspond bien au nombre de mélodies M, cela signifie qu'on a trouvé une solution pour chacune de celles attendues.
if len(ans) == M:
    # Pour chaque score dans 'ans', on l'affiche sur une nouvelle ligne.
    [print(i) for i in ans]
# Sinon (il manque au moins un score à renvoyer), on affiche -1 pour signaler l'impossibilité.
else:
    print(-1)