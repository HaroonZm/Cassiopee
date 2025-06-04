import bisect

def read_input():
    """
    Lit les paramètres principaux de l'utilisateur ainsi que la liste des positions,
    puis retourne ces valeurs.

    Retourne :
        n (int): la taille du cercle.
        m (int): le nombre de positions.
        p (int): la position de référence.
        d (list): liste des distances ajustées (modulo n) à partir de p.
    """
    # Lecture des trois entiers principaux depuis l'entrée standard
    n, m, p = map(int, raw_input().split())
    d = []  # Liste qui va contenir les distances transformées
    for i in xrange(m):
        inp = int(raw_input())  # Lecture d'une position
        # Calcul de la distance ajustée au point de référence et normalisation sur le cercle
        adjusted = (inp - p + n) % n
        d.append(adjusted)
    return n, m, p, d

def compute_minimal_distance(n, m, d):
    """
    Calcule la plus petite distance possible en prenant chaque position et en effectuant une rotation
    autour du cercle, basée sur la transformation précédente de la liste des positions.

    Args:
        n (int): taille du cercle.
        m (int): nombre de positions.
        d (list): liste des distances ajustées, déjà modulo n.

    Retourne :
        ans (int): la plus petite distance possible trouvée.
    """
    d.sort()  # Trie les positions pour permettre les traitements par intervalles
    # Initialisation de la variable de réponse avec la plus petite valeur entre
    # la plus grande position et la "distance circulaire" d'une tour à la suivante
    ans = min(d[-1], n - d[0])
    # Parcours pour évaluer la distance minimale pour chaque intervalle de la liste triée
    for i in xrange(m - 1):
        # Cas où on considère l'intervalle de i à i+1 sur le cercle, puis on effectue deux parcours
        # sur le cercle pour mesurer différentes distances possibles
        ans = min(ans, d[i] + (d[i] + n - d[i + 1]))
    for i in xrange(m - 1):
        # Cas symétrique précédent : partant de la fin pour revenir au début
        ans = min(ans, (n - d[i + 1]) + (n - d[i + 1] + d[i]))
    return ans

def main():
    """
    Fonction principale du script qui orchestre la lecture, le calcul et l'affichage du résultat.
    """
    # Lecture des paramètres et transformation initiale
    n, m, p, d = read_input()
    # Calcul de la distance minimale selon la logique du problème
    ans = compute_minimal_distance(n, m, d)
    # Affichage du résultat multiplié par 100 comme spécifié
    print ans * 100

# Exécution du programme principal
if __name__ == '__main__':
    main()