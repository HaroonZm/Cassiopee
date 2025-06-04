def read_input():
    """
    Lit les entrées utilisateur pour construire la liste l et déterminer la plus grande valeur dans chaque ligne.
    
    Returns:
        l (list of list of int): Liste d'entrée où chaque sous-liste représente une ligne de valeurs.
        max_value (int): La plus grande valeur rencontrée à la dernière position de chaque ligne.
    """
    n = int(input())  # Nombre de lignes à traiter
    l = []            # Cette liste va contenir toutes les lignes d'entrée
    max_value = 0     # Pour suivre la plus grande valeur rencontrée
    for _ in range(n):
        a = list(map(int, input().split()))  # Convertit la ligne saisie en liste d'entiers
        l.append(a)                          # Ajoute la sous-liste à la liste principale
        # Actualise max_value si la dernière valeur de la ligne courante est plus grande
        if a[-1] > max_value:
            max_value = a[-1]
    return l, max_value

def initialize_matrix(rows, cols):
    """
    Crée une matrice (liste de listes) de zéros de taille rows x cols.
    
    Args:
        rows (int): Nombre de lignes de la matrice.
        cols (int): Nombre de colonnes de la matrice.
    
    Returns:
        list: Matrice rows x cols initialisée à 0.
    """
    return [[0 for _ in range(cols)] for _ in range(rows)]

def fill_matrix(l, ans):
    """
    Remplit la matrice binaire 'ans' à partir de la liste l. Pour chaque sous-liste de l, 
    si la seconde valeur est supérieure à 0, marque à 1 les colonnes correspondant aux valeurs
    apparaissant à partir du troisième élément.
    
    Args:
        l (list of list of int): Liste des entrées utilisateur pour chaque ligne.
        ans (list of list of int): Matrice binaire à remplir.
    """
    n = len(l)  # Nombre de lignes à traiter
    for i in range(n):
        # Vérifie que le deuxième élément est positif
        if l[i][1] > 0:
            # Parcourt tous les éléments à partir du 3ème dans la sous-liste
            for j in range(2, len(l[i])):
                index = l[i][j] - 1  # Les indices dans ans commencent à 0
                ans[i][index] = 1    # Met la valeur correspondante à 1

def print_matrix(ans):
    """
    Affiche la matrice ligne par ligne sous forme de chaînes.
    
    Args:
        ans (list of list of int): Matrice à afficher.
    """
    for row in ans:
        print(" ".join(map(str, row)))

def main():
    """
    Fonction principale orchestrant la lecture des données, l'initialisation, le remplissage,
    et l'affichage de la matrice binaire.
    """
    # Lire les données d'entrée et trouver la plus grande valeur rencontrée à la fin des lignes
    l, max_value = read_input()
    n = len(l)
    # Initialiser la matrice réponse avec des zéros
    ans = initialize_matrix(n, max_value)
    # Remplir la matrice réponse selon la logique spécifiée
    fill_matrix(l, ans)
    # Afficher la matrice résultante
    print_matrix(ans)

# Lancement du programme
if __name__ == "__main__":
    main()