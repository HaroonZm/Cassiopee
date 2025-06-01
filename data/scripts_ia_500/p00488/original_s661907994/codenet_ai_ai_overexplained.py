# Importation du module sys qui permet d'interagir avec l'interpréteur Python et ses fonctionnalités
import sys
# Importation spécifique de la fonction stdin depuis le module sys; stdin représente le flux d'entrée standard (typiquement le clavier ou un fichier redirigé)
from sys import stdin
# Redéfinition de la fonction 'input' pour utiliser stdin.readline qui lit une ligne entière du flux d'entrée standard, incluant le caractère de fin de ligne
input = stdin.readline

# Définition de la fonction principale 'main' qui prend en argument une liste de paramètres 'args' (même si ici ils ne sont pas utilisés)
def main(args):
    # Création de la liste 'pastas' contenant trois entiers lus à partir de l'entrée standard
    # La compréhension de liste itère 3 fois (pour chacune des 3 sortes de pâtes)
    # À chaque itération, input() lit une ligne (une chaîne de caractères), 
    # int() convertit cette chaîne en un entier, et ce dernier est ajouté à la liste
    pastas = [int(input()) for _ in range(3)]

    # Création de la liste 'drinks' contenant deux entiers lus à partir de l'entrée standard,
    # même principe que pour 'pastas', mais cette fois avec 2 itérations
    drinks = [int(input()) for _ in range(2)]

    # Calcul du total minimal en sélectionnant le prix minimum dans la liste 'pastas' grâce à min(pastas)
    # et le prix minimum dans la liste 'drinks' grâce à min(drinks)
    # Ensuite, on soustrait 50 du total selon l'énoncé (réduction offerte)
    total = min(pastas) + min(drinks) - 50

    # Affichage du résultat à l'écran avec print()
    # La fonction print convertit automatiquement l'entier 'total' en chaîne de caractères et l'écrit sur la sortie standard
    print(total)

# Condition spéciale qui vérifie si ce fichier est exécuté en tant que script principal
# __name__ est une variable spéciale de Python; elle vaut '__main__' quand ce script est lancé directement
if __name__ == '__main__':
    # Appel de la fonction main en lui passant la liste des arguments de la ligne de commande à partir du deuxième élément (indice 1)
    # sys.argv est la liste des arguments; sys.argv[0] est toujours le nom du script; on passe donc sys.argv[1:] pour ne passer que les arguments utiles
    main(sys.argv[1:])