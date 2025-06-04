#!/usr/bin/python

# Importation du module 're' qui permet d'utiliser les expressions régulières
import re

def main():
    # Demande un nombre entier à l'utilisateur via l'entrée standard (console)
    # raw_input() lit la ligne entrée par l'utilisateur sous forme de chaîne de caractères
    # int() convertit cette chaîne en un entier
    n = int(raw_input())

    # Demande à l'utilisateur d'entrer une chaîne de caractères, stockée dans la variable 's'
    s = raw_input()

    # Utilisation de l'expression régulière r'^<*' :
    # - Le symbole '^' indique le début de la chaîne
    # - '<*' signifie zéro ou plusieurs signes '<'
    # L'appel re.search(r'^<*', s) retourne l'objet match correspondant au plus grand préfixe de '<'
    match_start = re.search(r'^<*', s)

    # Utilisation de l'expression régulière r'>*$' :
    # - '>*' signifie zéro ou plusieurs signes '>'
    # - '$' indique la fin de la chaîne
    # L'appel re.search(r'>*$', s) retourne l'objet match correspondant au plus grand suffixe de '>'
    match_end = re.search(r'>*$', s)

    # Pour chaque objet match, on calcule la longueur de la sous-chaîne trouvée :
    # - x.end() donne l'index juste après la fin du match
    # - x.start() donne l'index du début du match
    # - La différence x.end() - x.start() donne la longueur de la séquence trouvée
    # map() applique la fonction lambda à chaque objet match de la liste [match_start, match_end]
    lengths = map(lambda x: x.end() - x.start(), [match_start, match_end])

    # La fonction min() trouve la plus petite longueur parmi celles des séquences au début et à la fin
    min_length = min(lengths)

    # On calcule la valeur n - min_length, c'est-à-dire on soustrait la longueur minimale parmi les
    # séquences consécutives de '<' au début et de '>' à la fin à la valeur entière n.
    result = n - min_length

    # Affichage du résultat final à l'utilisateur
    print result

# Ce bloc s'assure que la fonction main() n'est exécutée que si ce script est lancé directement,
# c'est-à-dire, non importé comme module dans un autre script.
if __name__ == '__main__':
    main()