import sys  # Importation du module sys qui permet d'interagir avec l'interpréteur Python
from sys import stdin  # Importation spécifique de stdin, le flux d'entrée standard pour lecture
from itertools import product  # Importation de la fonction product qui génère le produit cartésien d'itérables
input = stdin.readline  # Redéfinition de la fonction input pour lire une ligne depuis stdin de manière efficace

# Définition d'une fonction pour vérifier si un nombre est premier
def is_prime(n):
    # Si n est inférieur à 2, cela ne peut pas être un nombre premier (les premiers sont >= 2)
    if n < 2:
        return False
    # Le cas particulier du nombre 2 qui est le plus petit nombre premier pair
    if n == 2:
        return True
    # Tous les nombres pairs autres que 2 ne sont pas premiers
    if n % 2 == 0:
        return False
    # Boucle pour tester tous les diviseurs impairs possibles de 3 jusqu'à la racine carrée de n inclusive
    # La racine carrée est la limite parce qu'un facteur plus grand que sqrt(n) aurait un partenaire plus petit que sqrt(n)
    for i in range(3, int(n**0.5) + 1, 2):
        # Si n est divisible par i sans reste, il n'est pas premier
        if n % i == 0:
            return False
    # Si aucun diviseur n'a été trouvé, le nombre est premier
    return True

# Fonction principale de résolution qui prend deux entiers n et c selon l'énoncé
def solve(n, c):
    # Construction d'une valeur de retour par défaut (dummy), qui est un grand nombre formé de chiffres 9,
    # cette valeur est utilisée si aucune solution ne correspond aux critères
    # Pour c >= 0, on crée une chaîne composée de n '9', suivi de c, puis à nouveau n '9'
    if c >= 0:
        dummy = int('9' * n + str(c) + '9' * n)
    else:
        # Si c est négatif, on crée une chaîne composée seulement de 2n '9' (pas de chiffre central)
        dummy = int('9' * n + '9' * n)

    # Selon l'analyse issue d'une ressource en ligne (lien dans le code d'origine),
    # pour n > 4, la recherche devient trop coûteuse, donc on renvoie directement dummy
    if n > 4:
        return dummy

    found = False  # Variable booléenne pour marquer si on a trouvé un nombre premier correspondant
    ans = -1  # Variable pour stocker le résultat temporaire

    # Utilisation de product pour générer toutes les combinaisons de chiffres de longueur n à partir des chiffres '9' à '0'
    # Cela produit tous les tuples possibles de longueur n avec ces caractères
    for p in product('9876543210', repeat=n):
        # Le premier chiffre ne peut pas être '0' car cela produirait un nombre avec des zéros à gauche non valides
        if p[0] == '0':
            continue  # On ignore ces combinaisons

        # Conversion du tuple p en chaîne de caractères, reconstituant un nombre à n chiffres
        t = ''.join(p)

        # Selon la valeur de c, on construit un palindrome :
        # Si c >= 0, palindrome de la forme t + c + t inversé
        # Sinon, palindrome de la forme t + t inversé (pas de chiffre central)
        if c >= 0:
            ans = int(t + str(c) + t[::-1])
        else:
            ans = int(t + t[::-1])

        # Test de primalité du palindrome construit
        if is_prime(ans):
            found = True  # On a trouvé un palindrome premier correspondant aux critères
            break  # Sortie de la boucle dès qu'un nombre premier est trouvé

    # Si on a trouvé un tel palindrome premier, on le retourne
    if found:
        return ans
    else:
        # Sinon, on retourne la valeur par défaut dummy
        return dummy

# Fonction main qui sert de point d'entrée principal du script
def main(args):
    # Lecture d'une ligne d'entrée qui contient deux entiers séparés par un espace, 
    # utilisant la fonction input redéfinie plus haut pour une lecture efficace
    n, c = map(int, input().split())

    # Appel de la fonction solve avec les paramètres lus
    result = solve(n, c)

    # Affichage du résultat retourné par la fonction solve sur la sortie standard
    print(result)

# Condition pour vérifier que ce script est exécuté directement (pas importé comme module)
if __name__ == '__main__':
    main(sys.argv[1:])  # Appel de la fonction main avec les arguments de la ligne de commande ignorés ici car non utilisés