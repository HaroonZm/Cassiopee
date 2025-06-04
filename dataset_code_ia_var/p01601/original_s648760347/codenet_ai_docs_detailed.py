def find_nearest_palindrome(n):
    """
    Trouve et affiche le palindrome numérique le plus proche du nombre donné 'n'.
    Si deux palindromes sont à égale distance, le plus petit est choisi.
    
    Args:
        n (str): Le nombre d'entrée sous forme de chaîne de caractères.
    """
    i = 0  # Définir l'écart initial par rapport à n à zéro
    while True:  # Boucle infinie jusqu'à ce qu'un palindrome soit trouvé
        n1, n2 = str(int(n) - i), str(int(n) + i)  # Calculer les deux nombres à la même distance de n
        # Vérifier si n1 (n-i) est un palindrome
        if n1 == n1[::-1]:
            print(n1)  # Afficher le palindrome trouvé
            break  # Sortir de la boucle une fois le palindrome trouvé
        # Vérifier si n2 (n+i) est un palindrome
        elif n2 == n2[::-1]:
            print(n2)  # Afficher le palindrome trouvé
            break  # Sortir de la boucle une fois le palindrome trouvé
        i += 1  # Incrémenter l'écart pour vérifier les nombres suivants

def main():
    """
    Fonction principale pour exécuter la recherche du palindrome le plus proche.
    Elle lit l'entrée utilisateur et appelle la fonction de recherche.
    """
    n = input()  # Lire l'entrée utilisateur
    find_nearest_palindrome(n)  # Lancer la recherche et affichage du résultat

if __name__ == "__main__":
    main()