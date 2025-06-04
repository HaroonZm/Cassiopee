def read_input():
    """
    Lit les dimensions d'une matrice et les valeurs associées depuis l'entrée standard.
    
    Retourne :
        h (int) : Nombre de lignes de la matrice.
        w (int) : Nombre de colonnes de la matrice.
        a (list of list of int) : La matrice contenant les entiers lus.
    """
    # Lire les dimensions de la matrice
    h, w = map(int, input().split())
    # Lire chaque ligne de la matrice
    a = [list(map(int, input().split())) for _ in range(h)]
    return h, w, a

def compute_minimum_cost(h, w, a):
    """
    Calcule le coût minimal selon la formule :
    Pour chaque cellule (i, j), on considère la somme sur toutes les cellules (k, l) de
    min(|i-k|, |j-l|) * a[k][l], puis on retourne le minimum de ces sommes.

    Paramètres :
        h (int) : Nombre de lignes de la matrice.
        w (int) : Nombre de colonnes de la matrice.
        a (list of list of int) : Matrice des coefficients.

    Retourne :
        ans (int) : Le coût minimal calculé.
    """
    # Initialiser la variable de réponse avec une valeur suffisamment grande
    ans = 1010101010

    # Étudier chaque position (i, j) comme point de référence
    for i in range(h):
        for j in range(w):
            now = 0  # Coût associé à la position (i, j)
            # Parcourir toutes les cases de la matrice
            for k in range(h):
                for l in range(w):
                    # Ajouter la contribution de la cellule (k, l) selon la formule
                    now += min(abs(i - k), abs(j - l)) * a[k][l]
            # Mettre à jour le coût minimal si l’on trouve mieux
            ans = min(ans, now)
    return ans

def main():
    """
    Fonction principale qui orchestre la lecture des données, le calcul et l'affichage du résultat.
    """
    # Lire la matrice
    h, w, a = read_input()
    # Calculer le coût minimal selon la formule imposée
    ans = compute_minimum_cost(h, w, a)
    # Afficher la réponse
    print(ans)

# Lancer le programme principal
if __name__ == "__main__":
    main()