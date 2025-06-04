#!/usr/bin/env python3
# Bitset 1 - Bit Operation 1

# Cette fonction principale exécutera toutes les opérations demandées.
def run():
    # Lecture de la valeur entière saisie par l'utilisateur via la fonction input().
    # input() lit une chaîne au clavier, int(...) la convertit en entier.
    n = int(input())  # Par exemple, si l'utilisateur entre '5', alors n prendra la valeur entière 5.

    # Création d'un format de chaîne, stockée dans la variable fmt.
    # Le format "{:032b}" est une 'f-string' avancée qui transformera le nombre en une chaîne de 32 caractères représentant le nombre en binaire.
    # - 032 signifie que le nombre sera rempli de zéros ('0') à gauche jusqu'à obtenir une longueur de 32 caractères.
    # - 'b' signifie que le nombre sera formaté en base 2 (binaire).
    fmt = "{:032b}"

    # Affiche la représentation binaire du nombre entier entré par l'utilisateur, sur 32 bits.
    # fmt.format(n) retourne la chaîne binaire en utilisant le format défini préalablement.
    print(fmt.format(n))

    # Effectue l'opération de complément à un sur n avec inversion des bits :
    # - L'opérateur ~ effectue un NOT bit-à-bit sur n, renverse chaque bit : 0 <-> 1
    # - Cependant, en Python, les entiers sont signés et de taille arbitraire :
    #   ~n retourne -n-1, ce qui peut donner un résultat négatif et une longueur infinie en binaire
    #   On veut émuler un complément à un sur 32 bits.
    # - En ajoutant 2**32, on "masque" avec 32 bits (car 2**32 = 4294967296)
    #   Donc ~n + 2**32 donne l'inverse binaire de n sur 32 bits.
    print(fmt.format(~n + 2**32))

    # Décalage à gauche :
    # - n << 1 décale tous les bits de n d'une position vers la gauche (multiplie par 2),
    #   ce qui revient à ajouter un 0 à la fin de la représentation binaire (à droite).
    # - Cependant, si n utilise déjà 32 bits, décaler à gauche pourrait dépasser cette taille,
    #   donc on doit s'assurer de ne conserver que les 32 bits pondérés.
    # - (1 << 32) crée un nombre binaire avec un seul '1' au 33e bit en partant de la droite.
    # - ~ (1 << 32) inverse ce nombre, ce qui donne une suite de 32 '1' suivis d'un '0' en 33e position.
    # - Le '&' (AND bit-à-bit) entre n << 1 et ce masque permet de ne garder que les 32 premiers bits 
    #   et d'éliminer toute éventuelle retenue au-delà du 32e bit.
    print(fmt.format(n << 1 & ~(1 << 32)))

    # Décalage à droite :
    # - n >> 1 décale tous les bits de n d'une position vers la droite (divise par 2 entière),
    #   ce qui revient à supprimer le bit de poids le plus faible (à droite).
    # - C'est un simple décalage logique à droite.
    print(fmt.format(n >> 1))

# Point d'entrée du programme :
# Cette condition garantit que la fonction run() ne sera exécutée que si ce fichier
# est lancé directement dans l'interpréteur Python, et non s'il est importé comme module.
if __name__ == '__main__':
    run()