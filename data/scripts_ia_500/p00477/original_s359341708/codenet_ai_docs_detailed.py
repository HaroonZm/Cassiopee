def main():
    """
    Programme qui effectue deux opérations principales :
    1. Lit quatre entiers depuis l'entrée standard, calcule leur somme.
    2. Divise cette somme par 60 pour déterminer combien de segments de 60 
       sont contenus dans cette somme, puis affiche le quotient et le reste.
    
    Le programme affiche ensuite :
    - Le nombre de segments complets de durée 60 dans la somme.
    - Le reste de la somme après retrait de ces segments.
    """
    # Initialisation de la variable "t" qui contiendra la somme des quatre entiers
    t = 0

    # Boucle pour lire 4 entiers depuis l'entrée standard
    for _ in range(4):
        y = int(input())  # Lecture d'un entier
        t += y  # Ajout de l'entier lu à la somme totale

    # Copie de la somme totale dans la variable "c" pour traitement ultérieur
    c = t

    # Initialisation de la variable "g" qui comptera le nombre de segments de 60
    g = 0

    # Boucle infinie qui décrémente "c" par 60 tant que "c" est positif ou nul
    # Chaque décrément correspond à un segment complet de durée 60
    while True:
        if c < 0:
            # Lorsque "c" devient négatif, on sort de la boucle
            break
        else:
            c -= 60  # Soustraction de 60 à "c"
            g += 1   # Incrémentation du compteur de segments

    # On décrémente g de 1 pour compenser la dernière incrémentation qui a eu lieu
    # alors que "c" est devenu négatif
    g -= 1

    # Affichage du nombre de segments complets de 60
    print(g)

    # Affichage du reste de la somme modulo 60 (partie restante après les segments complets)
    print(t % 60)


# Appel de la fonction principale
main()