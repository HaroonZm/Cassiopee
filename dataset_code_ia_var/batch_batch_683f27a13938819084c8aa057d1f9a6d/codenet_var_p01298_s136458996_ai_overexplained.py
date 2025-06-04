import sys  # Importe le module système pour lire les entrées et écrire les sorties

# Raccourcis pour les fonctions d'entrée et de sortie
readline = sys.stdin.readline   # Fonction pour lire une ligne depuis l'entrée standard (clavier ou fichier pipé)
write = sys.stdout.write        # Fonction pour écrire sur la sortie standard (écran ou fichier redirigé)

def solve():
    # Lit une ligne, la découpe en deux entiers (N et L)
    # N : nombre d'éléments (par exemple, d'intervalles)
    # L : une capacité initiale maximale (par exemple, un volume maximal)
    N, L = map(int, readline().split())
    
    # Cas particulier : N == 0 signifie qu'il n'y a plus de cas à traiter
    if N == 0:
        return False  # Arrête la boucle principale

    # Initialise 'ma' à 0, qui servira à stocker le maximum de la valeur 'u' pour chaque intervalle
    ma = 0

    # Construction de la liste 'P', qui contient N sous-listes,
    # chaque sous-liste contient 3 entiers (s, t, u)
    # Chaque ligne lue est découpée en 3 entiers correspondants à un intervalle
    P = [list(map(int, readline().split())) for i in range(N)]

    # Calcule le maximum de la troisième valeur (u) parmi toutes les listes de P
    # Cela se fait en générant tous les 'u' de chaque (s, t, u) de 'P' via compréhension de liste
    ma = max(u for s, t, u in P)

    # K représente vraisemblablement la durée totale considérée (ici 86400 secondes = 24h)
    K = 86400

    # EPS est un petit epsilon pour gérer les comparaisons flottantes
    EPS = 1e-8

    # Définition d'une fonction auxiliaire 'check' qui prend en entrée :
    # x : un taux que l'on teste
    # M : nombre d'itérations (par défaut 2)
    def check(x, M = 2):
        # 'rest' représente la capacité restante de base au début (initialement L)
        rest = L
        # Liste pour stocker, pour chaque itération i, la capacité finale obtenue
        R = [0]*M
        # On répète l'opération M fois
        for i in range(M):
            # 'prv' (previous) stocke la fin de l'intervalle précédent, initialisé à 0
            prv = 0
            # On parcourt chaque intervalle (s, t, u) de 'P'
            for s, t, u in P:
                # Entre 'prv' et 's', il n'y a pas de consommation (on recharge à taux x)
                # On ajoute au réservoir (s-prv)*x, mais on ne dépasse pas L
                rest = min(rest + (s - prv) * x, L)
                # Entre 's' et 't', un autre processus consomme 'u' à chaque seconde
                # Sur (t-s) secondes, le taux effectif de remplissage est (x-u)
                rest = min(rest + (t - s) * (x - u), L)
                # On avance 'prv' à la fin de cet intervalle
                prv = t
                # Si on tombe sous 0 à n'importe quel moment, x est trop petit, on échoue
                if rest < 0:
                    return 0  # Retourne 0 : échec
            # Après le dernier intervalle, il reste du temps jusqu'à K, on recharge à taux x
            rest = min(rest + (K - prv) * x, L)
            # On stocke le reste atteint à cette itération
            R[i] = rest
        # On vérifie que la variation entre l'avant-dernier et le dernier 'rest' est négligeable
        # Si c'est le cas, la solution est stable, donc retourne True
        return R[-2] - EPS < R[-1]

    # On commence la recherche binaire entre 'left' = 0 et 'right' = ma (le maximum de u)
    left = 0
    right = ma

    # Algorithme de dichotomie/recherche binaire pour trouver la plus petite valeur x telle que check(x) soit vraie
    while left + EPS < right:
        # Calcul du milieu de l'intervalle courant
        mid = (left + right) / 2
        # Si check(mid) est possible, c'est que x=mid est suffisamment grand, on cherche plus petit
        if check(mid):
            right = mid
        else:
            left = mid

    # À la sortie de la boucle, 'right' contient la valeur minimale de x trouvée à près EPS près
    # On écrit la réponse avec 16 chiffres après la virgule pour la précision
    write("%.016f\n" % right)
    return True  # Indique de continuer à traiter le prochain cas

# Boucle pour traiter tous les cas tant que solve() retourne True
while solve():
    ...  # '...' est un placeholder indiquant qu'il ne se passe rien ici (on boucle juste)