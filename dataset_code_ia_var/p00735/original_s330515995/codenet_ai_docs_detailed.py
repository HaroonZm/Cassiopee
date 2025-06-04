import math

def generate_custom_sieve(limit):
    """
    Crée une liste de nombres premiers (ou éléments 'True' selon des critères spéciaux)
    selon un crible modifié. Seuls les indices congrus à 1 ou 6 modulo 7 restent à 'True'.
    Ensuite, les multiples de chaque tel indice sont éliminés comme dans le crible d'Ératosthène.

    Args:
        limit (int): La borne supérieure du crible généré.

    Returns:
        list: La liste des entiers qui respectent les conditions du crible.
    """
    # Initialisation de la liste L d'une taille de (limit + 1) éléments à False
    L = [False] * (limit + 1)
    
    # Pour chaque entier, on ne considère 'True' que s'il est congru à 1 ou 6 modulo 7
    for i in range(1, limit):
        t = i % 7
        if t == 6 or t == 1:
            L[i] = True
    
    # On utilise une variante du crible d'Ératosthène pour supprimer les multiples
    for i in range(2, int(math.sqrt(limit))):
        if L[i]:
            j = 2
            while i * j <= limit:
                L[i * j] = False
                j += 1
    
    # On récupère la liste finale des indices pour lesquels L[index] est True
    result = [i for i in range(len(L)) if L[i]]
    return result

def find_divisors(n, custom_list):
    """
    Cherche dans la liste custom_list les éléments qui divisent n.

    Args:
        n (int): L'entier dont on cherche les diviseurs.
        custom_list (list): Une liste d'entiers candidats à la division.

    Returns:
        list: Les éléments de custom_list qui divisent n.
    """
    # On parcourt la liste custom_list (en ignorant le premier élément) pour trouver les diviseurs
    divisors = [str(i) for i in custom_list[1:] if n % i == 0]
    return divisors

def main():
    """
    Fonction principale : génère une liste filtrée selon la logique de crible, puis lit des entrées à l'utilisateur
    jusqu'à ce que 1 soit entré. Pour chaque nombre donné, affiche tous les éléments filtrés qui le divisent.
    """
    N = 300000
    # Génération de la liste customisée (crible modifié)
    L = generate_custom_sieve(N)

    while True:
        n = input()
        # Conversion de l'entrée utilisateur en entier
        try:
            n = int(n)
        except ValueError:
            # Ignore toute entrée qui n'est pas un entier
            continue
        # Sortie de la boucle si l'entrée vaut 1
        if n == 1:
            break
        # Recherche et affichage des diviseurs dans la liste criblée
        ans = find_divisors(n, L)
        # Affichage formaté du résultat
        print("%d: %s" % (n, " ".join(ans)))

if __name__ == "__main__":
    main()