def push(t, x):
    """
    Ajoute l'entier x à la séquence A[t] (stockée sous forme de chaîne de caractères).

    Args:
        t (int): Index de la séquence cible.
        x (int): Valeur entière à ajouter.
    """
    A[t].append(str(x))

def dump(t):
    """
    Ajoute l'état actuel de la séquence A[t] (sous forme de chaîne séparée par des espaces)
    à la liste des réponses 'ans', suivi d'un saut de ligne.

    Args:
        t (int): Index de la séquence à afficher.
    """
    ans.append(" ".join(A[t]))
    ans.append("\n")

def clear(t):
    """
    Vide la séquence A[t].

    Args:
        t (int): Index de la séquence à vider.
    """
    A[t] = []

# Liaison des entrées/sorties standard à des alias pratiques
readline = open(0).readline  # Pour lire une ligne de l'entrée standard
writelines = open(1, 'w').writelines  # Pour écrire plusieurs lignes sur la sortie standard

# Lecture de la première ligne : N (nombre de séquences), Q (nombre de requêtes)
N, Q = map(int, readline().split())

# Initialisation de la liste de réponses et des séquences
ans = []  # Contiendra les sorties 'dump'
A = [[] for _ in range(N)]  # Liste de N séquences (initialement vides)

# Création d'une table de fonctions pour accéder rapidement aux opérations par indice de type
C = [push, dump, clear].__getitem__

# Traitement des Q requêtes
for _ in range(Q):
    # Lecture d'une requête. Le premier entier est le type d'opération t (0: push, 1: dump, 2: clear)
    # Les éventuels arguments suivants sont les paramètres de cette opération
    t, *a = map(int, readline().split())
    # Appel de la fonction correspondant à t avec les arguments extraits de la requête
    C(t)(*a)

# Écriture de toutes les réponses enregistrées dans 'ans' sur la sortie standard
writelines(ans)