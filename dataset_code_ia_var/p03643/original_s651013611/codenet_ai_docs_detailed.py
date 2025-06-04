"""
Auteur : halo2halo
Date : 29 Janvier 2020
But : Ajouter le préfixe 'ABC' à une chaîne lue depuis l'entrée standard et afficher le résultat.
"""

import sys
import itertools  # Importé mais non utilisé dans ce code

def main():
    """
    Fonction principale du programme.
    Lit une chaîne de caractères depuis l'entrée standard, supprime les espaces de fin,
    ajoute le préfixe 'ABC' à la chaîne, puis affiche le résultat.
    """
    # Fonctions utilitaires pour lire depuis stdin en mode binaire
    read = sys.stdin.buffer.read
    readline = sys.stdin.buffer.readline
    readlines = sys.stdin.buffer.readlines

    # Lire la prochaine ligne de l'entrée standard, la décoder en UTF-8 et retirer les espaces à la fin
    S = readline().decode('utf8').rstrip()

    # Afficher la chaîne reçue préfixée de 'ABC'
    print('ABC' + S)

if __name__ == "__main__":
    main()