import sys  # Importe le module système, utile pour interagir avec les entrées/sorties standard et d'autres fonctions système

read = sys.stdin.read  # Crée un alias 'read' qui référence la fonction d'entrée standard pour tout lire, rarement utilisé ici
readlines = sys.stdin.readlines  # Crée un alias 'readlines' pour lire toutes les lignes depuis l'entrée standard

def main():
    # Demande à l'utilisateur d'entrer un nombre entier depuis l'entrée standard
    # La fonction input() lit une ligne de texte, puis int() convertit cette chaîne en un entier
    n = int(input())

    # Crée une liste vide nommée 'nums' pour stocker tous les puissances de 6 et 9 inférieures ou égales à n
    nums = []

    # Initialise une variable pour parcourir les puissances de 6, commence à 6
    n6 = 6

    # Boucle while pour ajouter toutes les puissances de 6 <= n à la liste 'nums'
    # Ex: 6, 36, 216, etc.
    while n6 <= n:
        nums.append(n6)  # Ajoute la puissance courante de 6 à la liste
        n6 = n6 * 6      # Multiplie la valeur courante de n6 par 6 pour passer à la puissance suivante

    # Initialise une variable pour parcourir les puissances de 9, commence à 9
    n9 = 9

    # Boucle while pour ajouter toutes les puissances de 9 <= n à la liste 'nums'
    # Ex: 9, 81, 729, etc.
    while n9 <= n:
        nums.append(n9)  # Ajoute la puissance courante de 9 à la liste
        n9 = n9 * 9      # Multiplie la valeur courante de n9 par 9 pour passer à la puissance suivante

    # Trie la liste 'nums' en ordre décroissant (du plus grand au plus petit) pour rendre les calculs potentiellement plus rapides
    nums.sort(reverse=True)

    # Initialise une liste 'dp' pour la programmation dynamique
    # dp[i] représentera le nombre minimal de pièces requises pour former le nombre i
    # On initialise dp[i] avec la valeur i, ce qui correspond au cas où on ne pourrait utiliser que des pièces de 1
    dp = [i for i in range(2 * n + 1)]
    # range(2 * n + 1) génère la séquence d'entiers de 0 à 2n inclus, soit (2n + 1) valeurs

    # Boucle sur chaque valeur dans 'nums', c'est-à-dire chaque pièce de type "puissance de 6 ou 9"
    for num in nums:
        # Pour chaque pièce 'num', on essaie de mettre à jour tous les dp pour les montants possibles
        for j1 in range(n + 1):
            # On essaie d'utiliser une nouvelle pièce 'num' pour former la somme j1 + num
            # On vérifie si utiliser la pièce 'num' diminue le nombre total de pièces nécessaires pour obtenir j1+num
            dp[j1 + num] = min(dp[j1 + num], dp[j1] + 1)

    # Affiche le nombre minimum de pièces nécessaires pour former le nombre 'n'
    print(dp[n])

# Ce bloc assure que la fonction main() n'est appelée que si le fichier est exécuté comme programme principal
# __name__ est une variable spéciale qui prend la valeur '__main__' quand le fichier est exécuté et non importé
if __name__ == '__main__':
    main()