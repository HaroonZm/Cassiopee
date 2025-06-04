from collections import deque  # Importe la classe deque du module collections, utile pour créer des files avec des opérations rapides d'ajout et retrait aux deux extrémités

# Lecture deux entiers séparés par un espace : 
# N représente le nombre d'intervalles, T un entier inutilisé dans le code actuel
N, T = map(int, input().split())

queue = deque()  # Création d'une file vide pour stocker les points d'événements (début et fin des intervalles)

# Boucle pour traiter chaque intervalle
for i in range(N):  # Itère N fois, où chaque i prendra successivement les valeurs de 0 à N-1
    l, r = map(int, input().split())  # Lecture de deux entiers, l et r, représentant respectivement les bornes gauche (début) et droite (fin) de l'intervalle
    queue.extend([(l, 1), (r, -1)])  # Ajoute deux tuples à la queue :
                                     # (l, 1) marque le début d'un segment (+1 à l'ouverture)
                                     # (r, -1) marque la fermeture d'un segment (-1 à la fermeture)

queue = sorted(queue)  # Trie la liste d'événements par ordre croissant de temps.
                       # Ceci est important pour traiter les événements dans l'ordre chronologique.

ans = 0  # Initialisation de la variable pour stocker le maximum actuel de segments ouverts (résultat final)
p = 0    # Initialisation de la variable pour suivre le nombre courant de segments ouverts

# Parcours séquentiel de tous les points d'événement
for t, s in queue:  # Décompresse chaque tuple : t est la position (temps ou point), s est le type d'événement (+1 pour ouverture, -1 pour fermeture)
    if s == 1:  # Si c'est un début d'intervalle
        p += 1  # Incrémente le compteur de segments ouverts
        ans = max(ans, p)  # Met à jour le maximum rencontré jusqu'ici si le nouveau compteur p est supérieur
    else:  # Sinon, c'est une fermeture d'intervalle
        p -= 1  # Décrémente le compteur de segments ouverts

# Affiche le résultat final
# Utilisation de max(ans, p) est redondante car p devrait être à 0 ici, mais cela couvre le cas où un bug aurait empêché la fermeture de tous les segments
print(max(ans, p))  # Affiche à l'écran le nombre maximal de segments ouverts simultanément